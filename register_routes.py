from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class Sugestao(BaseModel):
    id: int
    nome_colaborador: str
    setor: str
    descricao: str
    status: Literal["aberta", "em analise", "implementada"] = "aberta"
    data_criacao: datetime = datetime.now()

register_router = APIRouter(prefix="/register", tags=["register"])

db_sufestoes = []

@register_router.post("/")
async def criar_sugestao(sufestao: Sugestao):
    """
    Cria uma nova sugestão usando os campos fornecidos.
    """
    return {"Mensagem": "Você acessou a rota de criação de sugestão"}
