import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "usuarios.sqlite")
cursor = conexao.cursor()


def criar_tabela(cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?);", data
    )
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute(
        "UPDATE clientes SET nome=?, email=? WHERE id=?;", data
    )
    conexao.commit()


def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute(
        "DELETE FROM clientes WHERE id=?;", data
    )
    conexao.commit()


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany(
        "INSERT INTO clientes (nome, email) VALUES (?, ?)", dados
    )
    conexao.commit()


def recuperar_cliente(cursor, id):
    cursor.execute(
        "SELECT * FROM clientes WHERE id=?", (id,)
    )
    return cursor.fetchone()


def listar_clientes(cursor):
    cursor.execute(
        "SELECT * FROM clientes"
    )
    return cursor.fetchall()

