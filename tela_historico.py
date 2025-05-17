from rich.table import Table
from datetime import datetime
from rich.console import Console
from banco import conectar
import os


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Tela_historico(usuario_logado):
    from tela_menu import Tela_menu
    from colorama import Fore, Style

    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
    print(Fore.BLUE+"TELA HISTÓRICO"+Style.RESET_ALL)
        
    print("\n1 - DESAFIO ÁGUA")
    print("2 - DESAFIO RESÍDUOS")
    print("3 - DESAFIO ENERGIA")
    print("4 - DESAFIO TRANSPORTE")
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
    
    
    print("\n1 - TELA MENU")
    print("2 - MENU OPÇÕES")
    print("3 - Consultar resultado em determinada data")
    resposta = input(Fore.RED +"\nEscreva qual das opções você deseja?: "+ Style.RESET_ALL)
    
    if(resposta == "1"):
        limpar_terminal()
        Tela_menu(usuario_logado)
    if(resposta == "3"):
        limpar_terminal()
        data_desejada_string = input("\nDigite a data que deseja bucar suas informções de sustentabilidade!! (DD/MM/AAAA): ")
    
        try:
    
            data_desejada = datetime.strptime(data_desejada_string, "%d/%m/%Y").date()
    
        #conexao está pegando a função conectar do arquivo banco.py
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
            print("\nPara ", Fore.RED+"alterar"+Style.RESET_ALL ,"o valor que você forneceu em cada desafio, basta digitar o número correspondente ao desafio(",Fore.LIGHTYELLOW_EX+"1 para Água / 2 para Resíduos ..."+Style.RESET_ALL,")")
            print("Para", Fore.RED+" voltar "+Style.RESET_ALL, "ao MENU digite 5...")
            alter_desa = input("Digite o que deseja:...")
        
            conexao = conectar()
            cursor = conexao.cursor(dictionary=True)
            comando = "UPDATE respostas_desafios SET valor = %s, respostas = %s, pontuacao = %s WHERE id_usuario = %s AND id_desafio = %s" 

            if alter_desa == "2":
 
                consumoresiduos1=float(input("Quanto pesa seu lixo reciclável em gramas(g)? "))
                consumoresiduos2=float(input("Quanto pesa seu lixo não reciclável em gramas(g)? "))
            
            
            
                if (consumoresiduos1>consumoresiduos2*1.5):
                    residuos = "ALTA SUSTENTABILIDADE"
                    pontos2 = 10
                # Salva os dados no banco de dados
                    cursor.execute(comando, (consumoresiduos1,residuos,pontos2, usuario_logado["id"], alter_desa))
                    conexao.commit()
                
    

                elif ((consumoresiduos1>=consumoresiduos2*1.2) and (consumoresiduos1<=consumoresiduos2*1.5)):
                    residuos = "MODERADA SUSTENTABILIDADE"
                    pontos2 = 5
                # Salva os dados no banco de dados
                    cursor.execute(comando, (consumoresiduos1,residuos,pontos2, usuario_logado["id"], alter_desa))
                    conexao.commit()
                
                elif (consumoresiduos1<consumoresiduos2*0.8):
                    residuos = "BAIXA SUSTENTABILIDADE"
                    pontos2 = 2
                # Salva os dados no banco de dados
                    cursor.execute(comando, (consumoresiduos1,residuos,pontos2, usuario_logado["id"], alter_desa))
                    conexao.commit()

                else:
                    residuos = "BAIXA SUSTENTABILIDADE"
                    pontos2 = 2
                # Salva os dados no banco de dados
                    cursor.execute(comando, (consumoresiduos1,residuos,pontos2, usuario_logado["id"], alter_desa))
                    conexao.commit()
                    
                    
            elif alter_desa == "1":
            
                consumoagua = float(input("Qual o seu consumo de água em metros cúbicos (m³)? "))
                consumoagua1 = consumoagua * 1000  # Convertendo o consumo para litros
                
                if consumoagua1 < 150:
                    agua = "ALTA SUSTENTABILIDADE"
                    pontos1 = 10
                # Salva os dados no banco de dados
                    cursor.execute(comando, (consumoagua1,agua,pontos1, usuario_logado["id"], alter_desa))
                    conexao.commit()
                elif 150 <= consumoagua1 <= 200:
                    agua = "MODERADA SUSTENTABILIDADE"
                    pontos1 = 5
            # Salva os dados no banco de dados
                    cursor.execute(comando, (consumoagua1,agua,pontos1, usuario_logado["id"], alter_desa))
                    conexao.commit()
                
                else:
                    agua = "BAIXA SUSTENTABILIDADE"
                    pontos1 = 2
                # Salva os dados no banco de dados
                    cursor.execute(comando, (consumoagua1,agua,pontos1, usuario_logado["id"], alter_desa))
                    conexao.commit()
        
        
            elif alter_desa == "3":
                kwh = int(input("Digite quanto você gasta de energia em Kwh: "))
            
                if kwh < 5:
                    energia = "ALTA SUSTENTABILIDADE"
                    pontos3 = 10
                # Salva os dados no banco de dados
                    cursor.execute(comando, (kwh,energia,pontos3, usuario_logado["id"], alter_desa))
                    conexao.commit()

             
                elif 5 <= kwh <= 10:
                    energia = "MODERADA SUSTENTABILIDADE"
                    pontos3 = 5
                # Salva os dados no banco de dados
                    cursor.execute(comando, (kwh,energia,pontos3, usuario_logado["id"], alter_desa))
                    conexao.commit()
               
             
                else:
                    energia = "BAIXA SUSTENTABILIDADE"
                    pontos3 = 2
                # Salva os dados no banco de dados
                    cursor.execute(comando, (kwh,energia,pontos3, usuario_logado["id"], alter_desa))
                    conexao.commit()
                
            elif alter_desa == "4":
            
            
                print("\nPARA ATUALIZAR SELECIONE UMA OPÇÃO\n")
                print("1 - Sem gasto de combustíveis fósseis (a pé, bicicleta, patinete ou outro meio)")
                print("2 - Uso misto de transporte público e privado (ônibus, carona ou outro meio)")
                print("3 - Uso exclusivo e privado (veículo próprio)")
                print("")
    
                # Pede para o usuário digitar o seu transporte mais utilizado no dia atual e verifica se um valor válido foi digitado
                while True:
                    try:
                        meiotransporte = int(input("Digite uma das opções: "))
        
                        if meiotransporte == 1:
                            transporte = "Sem gasto de combustíveis fósseis"
                            pontos4 = 10
                            cursor.execute(comando, (0,transporte,pontos4, usuario_logado["id"], alter_desa))
                            conexao.commit()
                            break

                        elif meiotransporte == 2:
                            transporte = "Uso misto de transporte público e privado"
                            pontos4 = 5
                            cursor.execute(comando, (0,transporte,pontos4, usuario_logado["id"], alter_desa))
                            conexao.commit()
                            break

                        elif meiotransporte == 3:
                            transporte = "Uso exclusivo e privado"
                            pontos4 = 2
                            cursor.execute(comando, (0,transporte,pontos4, usuario_logado["id"], alter_desa))
                            conexao.commit()
                            break

                        else:
                            print("Digite uma opção válida (1, 2 ou 3).\n")
                            continue  # volta pro início do loop
                    
                    except ValueError:
                        print("\nErro: Digite um número válido.\n")

            elif alter_desa == "5":
                limpar_terminal()
                Tela_menu(usuario_logado)
            
            limpar_terminal()
            print("ATUALIZADO ✅")    
            Tela_historico(usuario_logado)
            
    if(resposta == "2"):
        from tela_desafios import Tela_opcoes
        limpar_terminal()
        Tela_opcoes(usuario_logado)