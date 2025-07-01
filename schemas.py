from pydantic import BaseModel
from typing import Optional
from enum import Enum

class UsuarioSchema(BaseModel):
    nome_colaborador : str
    email: str
    senha : str
    admin : Optional[bool]
    
    class Config:
        from_attributes = True

class SugestaoSchema(BaseModel):
    id : int
    nome_colaborador: str
    setor: str
    descricao: str
    status: str  = "aberta"
    class Config:
        from_attributes = True

# 1. Define os status permitidos de forma segura
class StatusSugestao(str, Enum):
    aberta = "aberta"
    em_analise = "em análise"
    implementada = "implementada"

# 2. Define o que a API espera receber no corpo da requisição
class SugestaoStatusUpdateSchema(BaseModel):
    status: StatusSugestao