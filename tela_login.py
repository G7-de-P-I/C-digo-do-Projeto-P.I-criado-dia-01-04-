import os

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
                usuario = input("\nDigite seu nome de usuário: ")
                senha = input("Digite sua senha: ")
        
                if(usuario == "admin" and senha == "admin"):
                    from tela_menu import Tela_menu
                    limpar_terminal()
                    Tela_menu()
                else:
                    print("\n Usuário ou senha errado")
            else:
                from tela_cadastro import Tela_cadastro
                limpar_terminal()
                print("\n----------------------------------------------------------------")
                print("REALIZE SEU CADASTRO PRIMEIRO")
                Tela_cadastro()
        except ValueError as e:
                    print(e)
                    print("Tente Novamente")