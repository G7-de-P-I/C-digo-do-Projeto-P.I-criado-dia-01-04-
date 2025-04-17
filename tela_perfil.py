import os



def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def Tela_perfil(usuario_logado):
    print("------------------------------------------------------------------")
    print("👤 PERFIL DO USUÁRIO")
    print("------------------------------------------------------------------")
    
    
    if usuario_logado:
        print(f"\nOlá {usuario_logado['nome']}, aqui estão algumas informações que podem ser úteis para você!!")
        print("\nNível sustentável de hoje: ...\n")
        print(f"ID: {usuario_logado['id']}")
        print(f"Nome: {usuario_logado['nome']}")
        print(f"E-mail: {usuario_logado['email']}")
        print(f"CPF: {usuario_logado['cpf']}")
        input("\nPara VOLTAR pressione Enter")
        limpar_terminal()
        from tela_menu import Tela_menu
        Tela_menu(usuario_logado)