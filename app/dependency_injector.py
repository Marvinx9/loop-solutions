from typing import Annotated
from fastapi import Depends

from app.data_base.local import LocalDataBase
from app.data_base.client_repository import ClientRepository

data_base = LocalDataBase()

def get_data_base() -> LocalDataBase:
    return data_base

def get_client_repository (data_base: Annotated[LocalDataBase, Depends(get_data_base)]) -> ClientRepository:
    return ClientRepository(data_base)