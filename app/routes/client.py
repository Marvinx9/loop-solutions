from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from app.models.client import Client, ClientCreateUpdate
from app.data_base.client_repository import ClientRepository
from app.dependency_injector import get_client_repository

router = APIRouter(prefix="/clients", tags=["Client"])

@router.get("/", status_code=200, response_model=list[Client])
async def list_clients(client_repository: Annotated[ClientRepository, Depends(get_client_repository)]):
    return await client_repository.list_clients()

@router.get("/{client_id}", status_code=200, response_model=Client | None)
async def get_client(client_repository: Annotated[ClientRepository, Depends(get_client_repository)], client_id: int):
    client = await client_repository.get_client(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    return client

@router.post("/", response_model=Client, status_code=201)
async def create_client(client_repository: Annotated[ClientRepository, Depends(get_client_repository)], client: ClientCreateUpdate):
    return await client_repository.create_client(client)

@router.put("/{client_id}", status_code=200, response_model=Client | None)
async def update_client(client_repository: Annotated[ClientRepository, Depends(get_client_repository)], client_id: int, client: ClientCreateUpdate):
    client_updated = await client_repository.update_client(client_id, client)
    if not client_updated:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    return client_updated

@router.delete("/{client_id}", status_code=204)
async def delete_client(client_repository: Annotated[ClientRepository, Depends(get_client_repository)], client_id: int):
    success = await client_repository.delete_client(client_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
