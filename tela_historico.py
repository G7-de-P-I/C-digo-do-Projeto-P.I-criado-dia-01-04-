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
        
    print("--------------------------------")
    print("1 - DESAFIO ÁGUA")
    print("2 - DESAFIO RESÍDUOS")
    print("3 - DESAFIO ENERGIA")
    print("4 - DESAFIO TRANSPORTE")
    print("--------------------------------")
    print(" ")
    
    data_desejada_string = input("Digite a data que deseja bucar suas informções de sustentabilidade!! (DD/MM/AAAA): ")
    
    try:
    
        data_desejada = datetime.strptime(data_desejada_string, "%d/%m/%Y").date()
    
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        comando = "SELECT data_resposta, pontuacao, respostas, id_desafio, valor FROM respostas_desafios WHERE id_usuario = %s AND data_resposta = %s ORDER BY data_resposta DESC"
        cursor.execute(comando, (usuario_logado["id"], data_desejada))
        dados = cursor.fetchall()
    
        console = Console()
        
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
    
    while True:
        alter_desa = input("\nPara alterar o valor que você forneceu em cada desafio, basta digitar o número correspondente ao desafio(1 para Água / 2 para Resíduos ...): \n")
        new_valor = float(input("Agora digite o novo valor: "))
        
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        
        
            
        comando = "UPDATE respostas_desafios SET valor = %s WHERE id_usuario = %s AND id_desafio = %s"
        cursor.execute(comando, (new_valor, usuario_logado["id"], alter_desa))
        conexao.commit()
        limpar_terminal()
        print("ATUALIZADO ✅")    
        Tela_historico(usuario_logado)