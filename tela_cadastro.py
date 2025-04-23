import os
from banco import conectar

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def Tela_cadastro():
    
    from tela_principal import Tela_principal
    cursor = None
    conexao = None
    
    print("")
    print("------------------------------------------------------------------")
    print("CADASTRO")
    print("------------------------------------------------------------------")
    
    nome = input("\n Nome: ")
    
    
    while True:
        email = input("\nEmail: ")
        if "@" in email and "." in email.split("@")[-1]:
            break
        else:
            print("❌ Email inválido! Digite um email no formato correto (ex: nome@exemplo.com).")
    
    while True:
        cpf = input("\nCPF (apenas números): ")
        if len(cpf) == 11:
            break
        else:
            print("❌ CPF inválido! Certifique-se de digitar 11 números.")

    senha = input("\n Senha: ") 
    
     
    try:
        #ele faz isso ...
        conexao = conectar()
        cursor = conexao.cursor()
        
        comando = "INSERT INTO usuario (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)"
        valores = (nome, email, cpf, senha)
        
        cursor.execute(comando, valores)
        conexao.commit()
        
        print("\n✅ Cadastro Realizado com Sucesso!") 
    except Exception as e:
        print(f"\n❌ Erro ao cadastrar: {e}")    
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
            
    input("\nPressione Enter para continuar")
    limpar_terminal()
    Tela_principal()