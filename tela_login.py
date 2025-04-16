import os
from banco import conectar


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def Tela_login():
    print("----------------------------------------------------------------")
    print("LOGIN")
    print("----------------------------------------------------------------")
    print("")
    print("Olá! Para começarmos nosso desafio, precisamos te conhecer!")

    while True:
        try:
            print("")
            resposta = input("Possui cadastro?(SIM/NÃO): ")
            
            if(resposta == "SIM" or resposta == "sim" or resposta == "Sim"):
                
                while True:
                    email = input("\nDigite seu email: ")
                    senha = input("Digite sua senha: ")
                
                    conexao = None
                    cursor = None 
                
                    try:
                        conexao = conectar()
                        cursor = conexao.cursor()
                    
                        comando = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
                        valores = (email, senha)
                    
                        cursor.execute(comando, valores)
                        usuario_logado = cursor.fetchone()
                    
                        if usuario_logado:
                            from tela_menu import Tela_menu
                            print("\n✅ Login realizado com sucesso!")
                            input("\nPressione Enter para continuar...")
                            limpar_terminal()
                            Tela_menu(usuario_logado)
                            break
                        else:
                            print("\n❌ Email ou senha incorretos!")
                            input("\nPressione Enter para tentar novamente...")
                            
                            
                    except Exception as e:
                        print(f"\n⚠️ Erro ao fazer login: {e}")
                    finally:
                        if cursor:
                            cursor.close()
                        if conexao:
                            conexao.close()

            else:
                from tela_cadastro import Tela_cadastro
                limpar_terminal()
                print("\n----------------------------------------------------------------")
                print("REALIZE SEU CADASTRO PRIMEIRO")
                Tela_cadastro()
        except ValueError as e:
                    print(e)
                    print("Tente Novamente")