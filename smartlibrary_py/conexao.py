import mysql.connector

from typing import cast
from mysql.connector import MySQLConnection


def conexao(
    endereco: str,
    usuario: str,
    senha: str,
    bancodedados: str
) -> MySQLConnection | None:

    try:
        connection = mysql.connector.connect(
            host=endereco,
            user=usuario,
            password=senha,
            database=bancodedados
        )

        return cast(MySQLConnection, connection)

    except mysql.connector.Error as err:
        print(f"Erro ao tentar se conectar ao banco de dados: {err}")
        return None


def fecharConexao(connection: MySQLConnection) -> None:
    if connection:
        connection.close()


def adicionarLivro(connection: MySQLConnection) -> None:
    cursor = connection.cursor()
    
    SQL = "INSERT INTO LIVROS (TITULO) VALUES (%s)"
    
    cursor.execute(SQL, )