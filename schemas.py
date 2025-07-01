from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

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
    data_criacao: datetime

    class Config:
        from_attributes = True

class StatusSugestao(str, Enum):
    aberta = "aberta"
    em_analise = "em análise"
    implementada = "implementada"

class SugestaoStatusUpdateSchema(BaseModel):
    status: StatusSugestao