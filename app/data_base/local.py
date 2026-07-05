import sqlite3
from contextlib import contextmanager

class LocalDataBase():
    def __init__(self, name_file='loop.db'):
        self.name_file = name_file
        self.initialize_database()

    @contextmanager
    def conect(self):
        conection = sqlite3.connect(self.name_file)
        try:
            yield conection
            conection.commit()
        except Exception as e:
            conection.rollback()
            raise e
        finally:
            conection.close()

    def initialize_database(self):
        with self.conect() as conection:
            cursor = conection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone TEXT NOT NULL
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL
                )
            ''')
