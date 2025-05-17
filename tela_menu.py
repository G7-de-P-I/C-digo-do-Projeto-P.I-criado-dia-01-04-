from rich.console import Console  # Biblioteca para saída estilizada no terminal (não utilizada aqui diretamente)
from tela_perfil import Tela_perfil  # Importa a tela de perfil
from tela_desafios import Tela_desafio  # Importa a tela de desafios
import os  # Biblioteca para executar comandos do sistema operacional
from colorama import Fore, Style # biblioteca para cores

# Função para limpar o terminal conforme o sistema operacional
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função principal do menu, recebe o usuário logado como parâmetro
def Tela_menu(usuario_logado):
    from tela_principal import Tela_principal, Tela_de_saida
    from tela_historico import Tela_historico  # Importa a tela de histórico (somente quando a função é chamada)
    
    # Exibe o menu principal com as opções disponíveis
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
    print(Fore.BLUE+"MENU"+Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
    print("\n1. DESAFIOS")  
    print("2. PERFIL")
    print("3. HÍSTORICO SUSTENTÁVEL")
    print("4. DESLOGAR")
    print("5. FECHAR PROGRAMA")
        
    # Laço para garantir entrada válida do usuário
    while True:
        try:
            Telair = int(input("\nDigite o número para ser direcionado para tela: "))
            
            # Redireciona para a tela de desafios
            if Telair == 1:
                limpar_terminal()
                Tela_desafio(usuario_logado)
            
            # Redireciona para a tela de perfil
            if Telair == 2:
                limpar_terminal()
                Tela_perfil(usuario_logado)
            
            # Redireciona para a tela de histórico
            elif Telair == 3:
                limpar_terminal()
                Tela_historico(usuario_logado)
            elif Telair == 4:
                limpar_terminal()
                Tela_principal()
            elif Telair == 5:
                limpar_terminal()
                Tela_de_saida()
            
            # Caso a opção não seja válida
            else:
                print("\n !!Opção inválida! Digite os números correspondentes!! ")  
        
        # Trata erro caso o usuário digite algo que não seja número
        except ValueError:
            print("\n------------------------------------------------------------------")
            print("\nTente Novamente")
