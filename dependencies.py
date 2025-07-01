from models import db
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
    """
    Cria e fornece uma sessão de banco de dados por requisição e garante que ela seja fechada no final
    """
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()