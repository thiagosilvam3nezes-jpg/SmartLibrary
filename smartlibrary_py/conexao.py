# em andamento
import mysql.connector

def conexao(endereco, usuario, senha, bancodedados):
    try:
        return mysql.connector.connect(
            host=endereco,
            user=usuario,
            password=senha,
            database=bancodedados
        )
    except mysql.connector.Error as err:
        print(f"Erro ao tentar se conectar ao banco de dados: {err}")
        return None
    
def fecharConexao(connection):
    if connection:
        connection.close()

def adicionarLivro(connection):
    cursor = connection.cursor()
        
    

