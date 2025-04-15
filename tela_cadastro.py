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
    email = input("\n Email: ")
    cpf = int(input("\n CPF: "))
    senha = input("\n Senha: ") 
    
    
    #pastel é bom
    
    
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        comando = "INSERT INTO usuario (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)"
        valores = (nome, email, cpf, senha)
        
        print("\n[DEBUG] Dados sendo enviados:", valores)
        
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