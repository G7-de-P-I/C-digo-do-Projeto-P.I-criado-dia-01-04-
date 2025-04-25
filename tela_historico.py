from rich.table import Table
from datetime import datetime
from rich.console import Console
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Tela_historico():
    from tela_menu import Tela_menu
    from tela_desafios import Tela_desafio
    
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    console = Console()
    
    t = Table(title = "\nHistórico de Sustentabilidade")
    
    t.add_column("Data", justify= "center", style="white")
    t.add_column("Pesquisa feita?", justify= "left", style="white")
    t.add_column("Nivel de Sustentabilidade", justify= "center", style="white")
    
    t.add_row("01/04/2025", "Pendente", "Indefinido")
    t.add_row("03/04/2025", "concluído", "Alto")
    
    console.print(t)
    
=======
=======
>>>>>>> Stashed changes
    
    print("--------------------------------")
    print("1 - DESAFIO ÁGUA")
    print("2 - DESAFIO ÁGUA")
    print("3 - DESAFIO ÁGUA")
    print("4 - DESAFIO ÁGUA")
    print("--------------------------------")
    print(" ")
    data_desejada_string = input("Digite a data que deseja bucar suas informções de sustentabilidade!! (DD/MM/AAAA): ")
    
    data_desejada = datetime.strptime(data_desejada_string, "%d/%m/%Y").date()
    
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    comando = "SELECT id_desafio, respostas, pontuacao, data_resposta, valor FROM respostas_desafios WHERE id_usuario = %s AND DATE(data_resposta) = %s"
    cursor.execute(comando, (usuario_logado["id"], data_desejada))
    dados = cursor.fetchall()
    
    console = Console()
    
    try:
        if dados:
            t = Table(title="\nHistórico de Sustentabilidade")

            t.add_column("N° DESAFIO", justify="left", style="white")
            t.add_column("RESPOSTA", justify="center", style="white")
            t.add_column("PONTUAÇÃO", justify="left", style="white")
            t.add_column("VALOR FORNECIDO", justify="center", style="white")
            t.add_column("DATA", justify="center", style="white")
    
        
            for linha in dados:
                desafio = str(linha['id_desafio'])
                resposta = str(linha['respostas'])
                valor = str(linha['valor'])
                pontuacao = str(linha['pontuacao'])
                data_formatada = linha['data_resposta'].strftime('%d/%m/%Y %H:%M')
                
                t.add_row(desafio, resposta, pontuacao,valor, data_formatada)
                
            console.print(t) 
        else:
            print(f"\nNenhum desafio foi respondido em {data_desejada.strftime('%d/%m/%Y')}.")
    except ValueError:
        print("Formato de data inválido. Use o formato DD/MM/AAAA.")
        
       
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
    
    while True:
        data_input = input("\n Caso deseje alterar algum desafio   ")
        
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
