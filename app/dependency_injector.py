from typing import Annotated
from fastapi import Depends

from app.data_base.local import LocalDataBase
from app.data_base.client_repository import ClientRepository
from app.data_base.user_repository import UserRepository

data_base = LocalDataBase()

def get_data_base() -> LocalDataBase:
    return data_base

def get_client_repository(data_base: Annotated[LocalDataBase, Depends(get_data_base)]) -> ClientRepository:
    return ClientRepository(data_base)

def get_user_repository(data_base: Annotated[LocalDataBase, Depends(get_data_base)]) -> UserRepository:
    return UserRepository(data_base)
