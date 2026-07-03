from fastapi import APIRouter
from app.models.client import Client

router = APIRouter(prefix="/clients")

LIST_CLIENTS = [
        Client(id_=1, nome="Afrânio", email="afranio@gmail.com", telefone="00311567894"),
        Client(id_=2, nome="Brena", email="brena@gmail.com", telefone="11311567894")
    ]

@router.get("/", response_model=list[Client])
async def list_clients():
    return LIST_CLIENTS

@router.get("/{client_id}", response_model=Client | None)
async def get_client(client_id: int):
    for client in LIST_CLIENTS:
        if client.id_ == client_id:
            return client
    return None