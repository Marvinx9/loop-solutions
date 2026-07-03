from pydantic import BaseModel

class Client(BaseModel):
    id_: int
    nome: str
    email: str
    telefone: str