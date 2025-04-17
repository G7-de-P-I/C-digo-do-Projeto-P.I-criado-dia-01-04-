from rich.table import Table
from datetime import datetime
from rich.console import Console
from banco import conectar
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Tela_historico(usuario_logado):
    from tela_menu import Tela_menu
    from tela_desafios import Tela_desafio
    
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    comando = "SELECT data_resposta FROM respostas_desafios WHERE id_usuario = %s ORDER BY data_resposta DESC"
    cursor.execute(comando, (usuario_logado["id"],))
    datas = cursor.fetchall()
    
    console = Console()
    
    t = Table(title="\nHistórico de Sustentabilidade")

    t.add_column("Sustentabilidade do dia", justify="left", style="white")
    t.add_column("Data", justify="center", style="white")

    if datas:
        for linha in datas:
            datas = linha['data_resposta']
            data_formatada = datas.strftime("%d/%m/%Y")
            # Você pode substituir "Pendente" por alguma lógica real de sustentabilidade
            t.add_row(usuario_logado['nome'], "Pendente", data_formatada)
    else:
        t.add_row(usuario_logado['nome'], "Sem dados", "-")

    console.print(t)        
    
    while True:
        data_input = input("\nDigite uma data (DD/MM/AAAA), caso deseje alterar as informações dos desafios!(PARA RETORNAR PRESS ENTER):  ")
        
        if(data_input == ""):
            limpar_terminal()
            Tela_menu(usuario_logado)
        try:
            data_formatada = datetime.strptime(data_input, "%d/%m/%Y").strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Formato inválido! Use DD/MM/AAAA.")
            
    limpar_terminal()
    
    print("MUDANDO INFORMAÇÕES DOS DESAFIOS - DIA { data chamada }")
    Tela_desafio(usuario_logado)
