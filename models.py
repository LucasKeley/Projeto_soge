from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.types import ChoiceType

# Criação do banco de dados
db = create_engine("sqlite:///database/banco.db")

# Certifique-se de que 'Base' está definida no seu arquivo de configuração do banco de dados (ex: database.py)
Base = declarative_base() # Se ainda não estiver definido em outro lugar

# --- 1. Classe para a Tabela de Usuários ---
class Usuario(Base):
    """
    Modelo ORM do SQLAlchemy para a tabela 'usuarios', representando
    um usuário que pode se autenticar no sistema e enviar sugestões.
    """
    __tablename__ = "usuarios" # Convenção: nome da tabela em minúsculas e no plural

    id = Column("id", Integer, primary_key=True, autoincrement=True) # ID único do usuário
    nome_colaborador = Column("nome_colaborador", String, nullable=False, index=True) # Nome completo do colaborador
    email = Column("email", String, unique=True, nullable=False, index=True) # E-mail do usuário (único)
    senha_hash = Column("senha_hash", String, nullable=False) # Hash da senha do usuário (nunca armazene a senha pura!)
    admin = Column("admin", Boolean, default=False, nullable=False) # Indica se o usuário tem privilégios de administrador
    data_cadastro = Column("data_cadastro", DateTime, default=datetime.now) # Data de criação do registro do usuário

    # Relacionamento: Um usuário pode ter várias sugestões
    sugestoes = relationship("Sugestao", back_populates="usuario")

    def __init__(self, nome_colaborador, email, senha_hash, admin=False):
        self.nome_cnome_colaborador =nome_colaborador
        self.email = email
        self.senha_hash = senha_hash
        self.admin = admin 

# --- 2. Classe para a Tabela de Sugestões ---
class Sugestao(Base):
    """
    Modelo ORM do SQLAlchemy para a tabela 'sugestoes', representando
    uma sugestão enviada por um colaborador (usuário).
    """
    __tablename__ = "sugestoes" # Convenção: nome da tabela em minúsculas e no plural

    id = Column("id", Integer, primary_key=True, autoincrement=True) # ID único da sugestão
    nome_colaborador = Column("nome_colaborador", ForeignKey("usuarios.id"))
    setor = Column("setor", String, nullable=False, index=True) # Setor da sugestão
    descricao = Column("descricao", String, nullable=False) # O texto detalhado da sugestão
    status = Column("status", String, nullable=False) # Status da sugestão: 'aberta', 'em análise', 'implementada'
    data_criacao = Column("data_criacao", DateTime, default=datetime.now) # Data e hora que a sugestão foi criada

    # Relacionamento: Uma sugestão pertence a um usuário
    usuario = relationship("Usuario", back_populates="sugestoes")

    def __init__(self, nome_colaborador, setor, descricao, status="aberta"):
        self.nome_colaborador = nome_colaborador
        self.setor = setor
        self.descricao = descricao
        self.status = status