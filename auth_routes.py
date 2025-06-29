from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    return {"Mensagem": "Você acessou a rota de autenticação", "autenticado": False}
