import os
import sqlite3

class Database:
    def __init__(self, db_name="loja.db"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.abspath(os.path.join(base_dir, "..", "data", db_name))
        self.conn = None
        self.cursor = None
        self.conectar()
        self.criar_tabelas()

    def conectar(self):
        """Abre conexão com o banco de dados"""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()

    def criar_tabelas(self):
        """Cria as tabelas se não existirem"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo_cliente TEXT CHECK(tipo_cliente IN ('PF', 'PJ')) NOT NULL,
                cpf TEXT,
                cnpj TEXT,
                data_nascimento TEXT,
                CHECK (
                    (tipo_cliente = 'PF' AND cpf IS NOT NULL AND cnpj IS NULL) OR
                    (tipo_cliente = 'PJ' AND cnpj IS NOT NULL AND cpf IS NULL)
                )
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_produto TEXT NOT NULL,
                codigo TEXT NOT NULL UNIQUE,
                preco_compra REAL NOT NULL,
                preco_venda REAL NOT NULL,
                estoque INTEGER NOT NULL
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                data TEXT NOT NULL,
                forma_pagamento TEXT NOT NULL CHECK(forma_pagamento IN ('Dinheiro', 'Cartão', 'Pix')),
                valor_total REAL NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens_venda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                venda_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                preco_unitario REAL NOT NULL,
                subtotal REAL NOT NULL,
                FOREIGN KEY (venda_id) REFERENCES vendas(id),
                FOREIGN KEY (produto_id) REFERENCES produtos(id)
            );
        """)
        self.conn.commit()

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
        if self.conn is None:
            self.conectar()
        self.cursor.execute(query, params)
        return self.cursor

    def fetchall(self):
        """Busca todos os resultados"""
        return self.cursor.fetchall()

    def fetchone(self):
        """Busca apenas um resultado"""
        return self.cursor.fetchone()
