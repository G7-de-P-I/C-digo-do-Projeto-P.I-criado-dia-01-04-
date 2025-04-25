from rich.console import Console  # Biblioteca para saída estilizada no terminal (não utilizada aqui diretamente)
from tela_perfil import Tela_perfil  # Importa a tela de perfil
from tela_desafios import Tela_desafio  # Importa a tela de desafios
import os  # Biblioteca para executar comandos do sistema operacional

# Função para limpar o terminal conforme o sistema operacional
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função principal do menu, recebe o usuário logado como parâmetro
def Tela_menu(usuario_logado):
    from tela_historico import Tela_historico  # Importa a tela de histórico (somente quando a função é chamada)
    
    # Exibe o menu principal com as opções disponíveis
    print("------------------------------------------------------------------")
    print("MENU")
    print("------------------------------------------------------------------")
    print("\n1. DESAFIOS")  
    print("2. PERFIL")
    print("3. HÍSTORICO SUSTENTÁVEL")
        
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
            
            # Caso a opção não seja válida
            else:
                print("\n !!Opção inválida! Digite os números correspondentes!! ")  
        
        # Trata erro caso o usuário digite algo que não seja número
        except ValueError:
            print("\n------------------------------------------------------------------")
            print("\nTente Novamente")
