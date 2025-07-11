from fastapi import APIRouter, HTTPException, Depends
from schemas import SugestaoSchema, SugestaoStatusUpdateSchema
from dependencies import pegar_sessao
from sqlalchemy.orm import Session
from models import Sugestao
from typing import List, Optional

register_router = APIRouter(prefix="/sugestoes", tags=["sugestoes"])

#1. Função da rota padrão
async def sugestoes():
    return {"mensagem": "Você acessou a rota de Sugestões"}

#2. Função de Criação de Sugestão
@register_router.post("/criar_sugestao")
async def criar_sugestao(sugestao_schema: SugestaoSchema, session: Session = Depends(pegar_sessao)):
    nova_sugestao = Sugestao(sugestao_schema.nome_colaborador, sugestao_schema.setor, sugestao_schema.descricao)
    session.add(nova_sugestao)
    session.commit()
    return {"Mensagem" : f"Sua Sugestão foi criada com sucesso. ID da sugestão: {nova_sugestao.id}"}

#3. Função para Listar todas as sugestões
@register_router.get("/listar_todas", response_model=List[SugestaoSchema])
async def listar_todas_sugestoes(session: Session = Depends(pegar_sessao)):
    """
    Retorna uma lista com todas as sugestões cadastradas.
    """
    todas_as_sugestoes = session.query(Sugestao).all()
    return todas_as_sugestoes

#4. Função de Filtragem por Status ou Setor
@register_router.get("/filtrar", response_model=List[SugestaoSchema])
async def filtrar_sugestoes(
    session: Session = Depends(pegar_sessao),
    setor: Optional[str] = None,
    status: Optional[str] = None,
):
    """
    Filtra as sugestões com base em um ou mais critérios opcionais.
    - setor: Filtra por nome exato do setor.
    - status: Filtra por status exato da sugestão.
    """
    # Inicia a consulta base
    query = session.query(Sugestao)
    # Aplica os filtros condicionalmente, apenas se eles forem fornecidos
    if setor:
        query = query.filter(Sugestao.setor == setor)
    if status:
        query = query.filter(Sugestao.status == status)
    sugestoes_filtradas = query.all()
    if not sugestoes_filtradas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma sugestão foi encontrada com os filtros aplicados."
        )
    return sugestoes_filtradas

#5. A função que atualiza o status
@register_router.patch("/{id}", response_model=SugestaoSchema)
async def atualizar_status_sugestao(
    id: int,
    status: SugestaoStatusUpdateSchema,
    session: Session = Depends(pegar_sessao)
):
    """
    Atualiza o status de uma sugestão específica.
    """
    # Busca no banco a sugestão com o ID fornecido
    sugestao_db = session.query(Sugestao).filter(Sugestao.id == id).first()
    # Se não encontrar, retorna um erro 404 (Not Found)
    if not sugestao_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sugestão com o ID {id} não foi encontrada."
        )
    # ATUALIZA O STATUS com o valor recebido na requisição
    sugestao_db.status = status.status.value
    # Salva a alteração no banco de dados
    session.commit()
    session.refresh(sugestao_db) # Atualiza o objeto com os dados do banco
    # Retorna a sugestão com o status já atualizado
    return sugestao_db