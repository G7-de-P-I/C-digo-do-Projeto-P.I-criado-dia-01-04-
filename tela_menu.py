from rich.console import Console
from tela_principal import Tela_perfil
from tela_desafios import Tela_desafio
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Tela_menu():
    from tela_historico import Tela_historico
    print("------------------------------------------------------------------")
    print("MENU")
    print("------------------------------------------------------------------")
    print("\n1. DESAFIOS")  
    print("2. PERFIL")
    print("3. HÍSTORICO SUSTENTÁVEL")
        
    while True:
        try:
            Telair = int(input("\nDigite o número para ser direcionado para tela: "))
               
            if (Telair == 1):
                    limpar_terminal()
                    Tela_desafio()
            if( Telair == 2):
                    limpar_terminal()
                    Tela_perfil()
            elif( Telair == 3):
                    limpar_terminal()
                    Tela_historico()
            else:
                    print("\n !!Opção inválida! Digite os números correpondentes!! ")  
               
        except ValueError:
                print("\n------------------------------------------------------------------")
                print("\nTente Novamente")