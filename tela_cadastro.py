import os # para limpar terminal
from banco import conectar # para conectar BD e enviar corretamente
import re # permite usar expressões regulares (para validar e-mail)


# Função que valida se o e-mail está no formato correto
def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Padrão básico de e-mail
    return re.match(padrao, email) is not None  # Retorna True se for válido


# Função para limpar o terminal (tela)
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # 'cls' para Windows, 'clear' para Linux/Mac


# Tela de cadastro de usuário
def Tela_cadastro():
    from tela_principal import Tela_principal  # Importa a função da tela principal (somente quando necessário)

    cursor = None
    conexao = None  # Prepara variáveis para a conexão com o banco
    
    # Título da tela
    print("")
    print("------------------------------------------------------------------")
    print("CADASTRO")
    print("------------------------------------------------------------------")
    
    # Pede o nome do usuário até que ele digite algo
    while True:
        nome = input("Nome: ")
        if not nome:
            print("❌ Por favor insira algum nome...")
        else:
            break

    # Pede o e-mail até que esteja no formato válido
    while True:        
        email = input("\nEmail: ")
        if validar_email(email):
            break
        else:
            print("❌ Email inválido! Digite um email no formato correto (ex: nome@exemplo.com).")
    
    # Pede o CPF com exatamente 11 números
    while True:
        cpf = input("\nCPF (apenas números): ")
        if len(cpf) == 11:
            break
        else:
            print("❌ CPF inválido! Certifique-se de digitar 11 números.")

    # Pede a senha (sem validação por enquanto)
    senha = input("\n Senha: ") 
    
    try:
        # Tenta conectar no banco e salvar os dados
        conexao = conectar()
        cursor = conexao.cursor()
        
        # Comando SQL para inserir os dados na tabela "usuario"
        comando = "INSERT INTO usuario (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)"
        valores = (nome, email, cpf, senha)  # Dados preenchidos pelo usuário
        
        cursor.execute(comando, valores)  # Executa o comando com os valores
        conexao.commit()  # Confirma a inserção no banco
        
        print("\n✅ Cadastro Realizado com Sucesso!")  # Mensagem de sucesso
    except Exception as e:
        # Se acontecer algum erro, mostra o erro
        print(f"\n❌ Erro ao cadastrar: {e}")    
    finally:
        # Fecha o cursor e a conexão, se tiverem sido abertos
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
            
    input("\nPressione Enter para continuar")  # Pausa antes de limpar
    limpar_terminal()  # Limpa a tela
    Tela_principal()  # Volta para a tela principal