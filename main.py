# para rodar o código, executar no terminal: uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from register_routes import register_router

app.include_router(auth_router)
app.include_router(register_router)

