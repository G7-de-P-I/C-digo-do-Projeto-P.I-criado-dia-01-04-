from rich.table import Table
from datetime import datetime
from rich.console import Console
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Tela_historico(usuario_logado):
    from tela_menu import Tela_menu
    from tela_desafios import Tela_desafio
    
    console = Console()
    
    t = Table(title = "\nHistórico de Sustentabilidade")
    
    t.add_column("Data", justify= "center", style="white")
    t.add_column("Pesquisa feita?", justify= "left", style="white")
    t.add_column("Nivel de Sustentabilidade", justify= "center", style="white")
    
    t.add_row("01/04/2025", "Pendente", "Indefinido")
    t.add_row("03/04/2025", "concluído", "Alto")
    
    console.print(t)
    
    
    while True:
        data_input = input("\nDigite uma data (DD/MM/AAAA), caso deseje alterar as informações dos desafios!(PARA RETORNAR PRESS ENTER):  ")
        
        if(data_input == ""):
            limpar_terminal()
            Tela_menu()
        try:
            data_formatada = datetime.strptime(data_input, "%d/%m/%Y").strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Formato inválido! Use DD/MM/AAAA.")
            
    limpar_terminal()
    
    print("MUDANDO INFORMAÇÕES DOS DESAFIOS - DIA { data chamada }")
    Tela_desafio()
