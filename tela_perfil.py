import os



def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def Tela_perfil(usuario_logado):
    print("------------------------------------------------------------------")
    print("👤 PERFIL DO USUÁRIO")
    print("------------------------------------------------------------------")
    
    
    if usuario_logado:
        id, nome, email, cpf, senha = usuario_logado
        print(f"\nOlá {nome}, aqui estão alguns informações que podem ser úteis para você!!")
        print("\nNível sustentável de hoje: ...\n")
        print(f"ID: {id}")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")
        input("\nPara VOLTAR pressione Enter")
        limpar_terminal()
        from tela_menu import Tela_menu
        Tela_menu(usuario_logado)