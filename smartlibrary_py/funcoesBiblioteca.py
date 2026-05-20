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
        
def cadastrarLivro(connection, SQL):
    
    cursor = connection.cursor(prepared=True)
    
    SQL = "INSERT INTO LIVROS(NOME, AUTOR, ISBN, DATAPUBLICACAO) VALUES(%s,%s,%s,%s)"
    
    dados = "A vida intelectual ,Antonin Dalmace Sertilenges, 9788539901890, 09/03/1920"
    
    
        