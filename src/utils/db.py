import os
import sqlite3


class Database:
    def __init__(self, db_name="loja.db"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.abspath(os.path.join(base_dir, "..", "data", db_name))
        self.conn = None
        self.cursor = None

    def conectar(self):
        """Abre conexão com o banco de dados"""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
        return self.cursor

    def commit(self):
        """Salva alterações"""
        if self.conn:
            self.conn.commit()

    def fechar(self):
        """Fecha conexão com o banco"""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

    def executar(self, query, params=()):
        """Executa uma query simples"""
        cur = self.conectar()
        cur.execute(query, params)
        return cur

    def fetchall(self):
        """Busca todos os resultados"""
        return self.cursor.fetchall()

    def fetchone(self):
        """Busca apenas um resultado"""
        return self.cursor.fetchone()
