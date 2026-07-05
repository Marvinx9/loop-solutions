from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.data_base.user_repository import UserRepository
from app.dependency_injector import get_user_repository

router = APIRouter(prefix="/login", tags=["Login"])

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html")

@router.post("/")
async def login(request: Request, user_repository: Annotated[UserRepository, Depends(get_user_repository)], email = Form(...), senha = Form(...)):
    user = await user_repository.get_user_by_email_senha(email, senha)
    if user:
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="session_token", value="token-senha", httponly=True)
        return response
    
    return templates.TemplateResponse(request, "login.html", {"email": email, "senha": senha, "error": "Credenciais inválidas"})
