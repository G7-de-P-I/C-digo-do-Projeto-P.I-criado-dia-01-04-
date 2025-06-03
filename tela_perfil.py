# Importa o módulo 'os' para executar comandos no terminal (como limpar a tela)
import os

# Importa a função 'conectar' do módulo 'banco', que será usada para conexão com o banco de dados
from banco import conectar

# Importa componentes do 'colorama' para estilizar o texto no terminal com cores
from colorama import Fore, Style

# Função para limpar o terminal (funciona tanto em Windows quanto em sistemas Unix)
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função que exibe as informações do perfil do usuário logado
def Tela_perfil(usuario_logado):
    # Imprime uma linha decorativa amarela
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
    
    # Imprime o título da tela de perfil com cor azul
    print(Fore.BLUE+"👤 PERFIL DO USUÁRIO"+Style.RESET_ALL)
    
    # Imprime outra linha decorativa amarela
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)



# Função que exibe a tela de perfil do usuário
def Tela_perfil(usuario_logado):
    # Exibe cabeçalho
    print("------------------------------------------------------------------")
    print("👤 PERFIL DO USUÁRIO")
    print("------------------------------------------------------------------") 
    
    # Verifica se há um usuário logado
    if usuario_logado:
        # Exibe uma saudação personalizada com o nome do usuário
        print(f"\nOlá {usuario_logado['nome']}, aqui estão algumas informações que podem ser úteis para você!!")
        # print("\nNível sustentável de hoje: ...\n")
        
        # Mostra um espaço reservado para o "nível sustentável de hoje" 
        print("\nNível sustentável de hoje: ...\n")
        
        # Exibe informações do usuário extraídas do dicionário: ID, nome, e-mail e CPF
        print(f"ID: {usuario_logado['id']}")
        print(f"Nome: {usuario_logado['nome']}")
        print(f"E-mail: {usuario_logado['email']}")
        print(f"CPF: {usuario_logado['cpf']}")
        
        # Aguarda o usuário pressionar Enter para retornar
        input(Fore.GREEN+"\nPara VOLTAR pressione Enter"+Style.RESET_ALL)
        
        # Limpa o terminal após o usuário pressionar Enter
        limpar_terminal()
        
        # Importa a função Tela_menu do módulo 'tela_menu', realiza a importação apenas quando necessário)
        from tela_menu import Tela_menu
        
        # Chama a função Tela_menu, passando novamente o usuário logado
        Tela_menu(usuario_logado)