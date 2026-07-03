from app.data_base.local import LocalDataBase
from app.models.client import Client

class ClientRepository:
    def __init__(self, data_base: LocalDataBase):
        self.db = data_base

    async def list_clients(self) -> list[Client]:
        with self.db.conect() as conection:
            cursor = conection.cursor()
            cursor.execute('''
                SELECT
                  id,
                  nome,
                  email,
                  telefone
                FROM clientes
            ''')
            rows = cursor.fetchall()
            clients = [
                Client(id_=row[0], nome=row[1], email=row[2], telefone=row[3])
                for row in rows
            ]

            return clients