from app.data_base.local import LocalDataBase
from app.models.user import User, UserCreateUpdate

class UserRepository:
    def __init__(self, data_base: LocalDataBase):
        self.db = data_base

    async def get_user_by_email_senha(self, email: str, senha: str) -> User | None:
        with self.db.conect() as conection:
            cursor = conection.cursor()
            cursor.execute('''
                SELECT
                  id,
                  nome,
                  email
                FROM usuarios
                WHERE email = ? AND senha = ?
            ''', (email, senha))
            row = cursor.fetchone()
            if row:
                return User(id_=row[0], nome=row[1], email=row[2])
            return None
        
    async def get_user_by_email(self, email: str) -> User | None:
        with self.db.conect() as conection:
            cursor = conection.cursor()
            cursor.execute('''
                SELECT
                  id,
                  nome,
                  email
                FROM usuarios
                WHERE email = ?
            ''', (email,))
            row = cursor.fetchone()
            if row:
                return User(id_=row[0], nome=row[1], email=row[2])
            return None

    async def create_user(self, create_user: UserCreateUpdate) -> User:
        with self.db.conect() as conection:
            cursor = conection.cursor()
            cursor.execute('''
                INSERT INTO usuarios (
                  nome,
                  email,
                  senha
                ) VALUES (
                    ?,
                    ?,
                    ?
                )
            ''', (create_user.nome, create_user.email, create_user.senha))
            id_ = cursor.lastrowid
            return User(id_=id_, nome=create_user.nome, email=create_user.email)
