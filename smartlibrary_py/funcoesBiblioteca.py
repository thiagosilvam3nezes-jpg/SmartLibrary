import mysql.connector

def ConexaoServidor(endereco: str, usuario: str, senha: str, data: str):
    try:
        connection = mysql.connector.connect(
            host=endereco,
            user=usuario,
            password=senha,
            database=data
        )
        
        print("Login realizado com sucesso!")
        return connection
        
    except mysql.connector.Error as erro:
        print(f"Nao foi possivel se conectar ao banco de dados", erro)
        
def encerrarConexao(connection):
    if connection:
        connection.close()
        