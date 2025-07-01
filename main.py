# para rodar o código, executar no terminal: uvicorn main:app --reload
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

#Carregamento de váriaveis do .env
load_dotenv()
#Configuração da SECRET_KEY 
SECRET_KEY = os.getenv("SECRET_KEY")
app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Importação das Rotas
from auth_routes import auth_router
from register_routes import register_router

#Inclui os roteadores na aplicação principal
app.include_router(auth_router)
app.include_router(register_router)