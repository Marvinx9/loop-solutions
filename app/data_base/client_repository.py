from app.data_base.local import LocalDataBase
from app.models.client import Client, ClientCreateUpdate

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
        
    async def get_client(self, client_id: int) -> Client | None:
        with self.db.conect() as conection:
            cursor = conection.cursor()
            cursor.execute('''
                SELECT
                  id,
                  nome,
                  email,
                  telefone
                FROM clientes
                WHERE id = ? 
            ''', (client_id,)
            )
            row = cursor.fetchone()
            if row:
                return Client(id_=row[0], nome=row[1], email=row[2], telefone=row[3])
            return None

    async def create_client(self, client: ClientCreateUpdate) -> Client | None:
        with self.db.conect() as conection:
            cursor = conection.cursor()
            cursor.execute('''
                INSERT INTO clientes (
                  nome,
                  email,
                  telefone
                ) VALUES (
                  ?,
                  ?,
                  ?
                )
            ''', (client.nome, client.email, client.telefone)
            )
            client_id = cursor.lastrowid
            return Client(id_=client_id, nome=client.nome, email=client.email, telefone=client.telefone)
        
    async def update_client(self, client_id: int, client: ClientCreateUpdate) -> Client | None:
        with self.db.conect() as conection:
            cursor = conection.cursor()
            cursor.execute('''
                UPDATE clientes
                SET
                  nome = ?,
                  email = ?,
                  telefone = ?
                WHERE id = ?
            ''', (client.nome, client.email, client.telefone, client_id)
            )
            if cursor.rowcount == 0:
                return None
            return Client(id_=client_id, nome=client.nome, email=client.email, telefone=client.telefone)
    
    async def delete_client(self, client_id: int) -> bool:
        with self.db.conect() as conection:
            cursor = conection.cursor()
            cursor.execute('''
                DELETE FROM clientes WHERE id = ?
                ''', (client_id,)
            )
            return cursor.rowcount > 0
