from src.utils.database import Database

db = Database()
db.criar_tabelas()
#db.executar("INSERT INTO clientes (nome, tipo_cliente, cpf, data_nascimento) VALUES (?, ?, ?, ?)", ("Padrão", "PF", "00000000000", "05/09/2025"))
cursor = db.executar("SELECT * FROM clientes")
#db.commit()
registros = cursor.fetchall()

for linha in registros:
    print(linha)

db.fechar()
