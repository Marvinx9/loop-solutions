from pydantic import BaseModel

class User(BaseModel):
    id_: int
    nome: str
    email: str
    senha: str | None = None
    
class UserCreateUpdate(BaseModel):
    nome: str
    email: str
    senha: str | None = None
