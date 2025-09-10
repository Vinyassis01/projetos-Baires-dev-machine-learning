import sqlite3

# Função para criar o banco de dados e a tabela
def criar_banco():
    conexao = sqlite3.connect("exemplo.db")
    cursor = conexao.cursor()

    # Criação da tabela
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS itens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()

# Função para adicionar itens ao banco de dados
def adicionar_item(nome, quantidade):
    conexao = sqlite3.connect("exemplo.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO itens (nome, quantidade) VALUES (?, ?)", (nome, quantidade))

    conexao.commit()
    conexao.close()

# Exemplo de uso
criar_banco()
adicionar_item("Item A", 10)
adicionar_item("Item B", 20)
print("Itens adicionados ao banco de dados!")