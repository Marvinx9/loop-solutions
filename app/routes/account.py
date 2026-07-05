from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.data_base.user_repository import UserRepository
from app.dependency_injector import get_user_repository
from app.models.user import UserCreateUpdate

router = APIRouter(prefix="/conta", tags=["Conta Usuário"])

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def account_page(request: Request):
    return templates.TemplateResponse(request, "registro.html")

@router.post("/")
async def create_user(request: Request, user_repository: Annotated[UserRepository, Depends(get_user_repository)], nome = Form(...), email = Form(...), senha = Form(...), confirma_senha = Form(...)):
    data = {"nome": nome, "email": email, "senha": senha, "confirma_senha": confirma_senha}

    if not all([nome, email, senha, confirma_senha]):
        return templates.TemplateResponse(request, "registro.html", {"error": "Campos obrigatórios faltantes", **data})

    user_exists = await user_repository.get_user_by_email(email)
    if user_exists:
        return templates.TemplateResponse(request, "registro.html", {"error": "Usuário inválido!", **data})

    create_user = UserCreateUpdate(nome=nome, email=email, senha=senha)
    user = await user_repository.create_user(create_user)

    if user:
        response = RedirectResponse(url="/login", status_code=303)
        return response
    return templates.TemplateResponse(request, "registro.html", {"error": "Não foi possível criar o usuário!", **data})
