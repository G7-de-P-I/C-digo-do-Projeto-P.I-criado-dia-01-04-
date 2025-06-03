# Importa a biblioteca que permite conectar ao banco de dados MySQL
import mysql.connector

# Função para conectar ao BD
def conectar():
    # Cria a conexão com o banco, usando os dados de acesso
    conexao = mysql.connector.connect(
        host="localhost",     # Endereço do banco (aqui é o próprio computador)
        user="root",          # Usuário do banco
        password ="",         # Senha do banco (aqui está em branco)
        database="projeto_pi" # Nome do banco de dados que será usado
    )
    # Retorna essa conexão para ser usada em outras partes do código
    return conexao