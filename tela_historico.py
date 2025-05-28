from rich.table import Table               # Importa a classe Table para exibir tabelas formatadas no terminal
from datetime import datetime             # Para manipulação e conversão de datas
from rich.console import Console          # Console para imprimir saída formatada no terminal
from banco import conectar                # Função para conectar ao banco de dados
import os                                 # Para comandos do sistema operacional, como limpar a tela
from tela_desafios import Salvar_no_Banco # Função para salvar dados no banco, caso necessário

# Função para limpar o terminal (compatível com Windows e Unix)
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal para exibir e alterar o histórico de sustentabilidade do usuário
def Tela_historico(usuario_logado):
    from tela_menu import Tela_menu         # Importa menu principal para navegação
    from colorama import Fore, Style        # Importa cores para impressão no terminal
    
    # Exibe título e cabeçalho da tela com cores
    print(Fore.LIGHTYELLOW_EX + "------------------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.BLUE + "TELA HISTÓRICO\n" + Style.RESET_ALL)
    
    # Menu inicial com opções de desafios para visualiz
    print("1 - DESAFIO ÁGUA")
    print("2 - DESAFIO RESÍDUOS")
    print("3 - DESAFIO ENERGIA")
    print("4 - DESAFIO TRANSPORTE")
    print(Fore.LIGHTYELLOW_EX + "------------------------------------------------------------------" + Style.RESET_ALL)
    
    # Menu inferior para outras opções
    print("\n1 - TELA MENU")
    print("2 - MENU OPÇÕES")
    print("3 - Consultar resultado em determinada data")
    resposta = input(Fore.RED + "\nEscreva qual das opções você deseja?: " + Style.RESET_ALL)
    
    # Se usuário quiser voltar para menu principal
    if resposta == "1":
        limpar_terminal()
        Tela_menu(usuario_logado)
        
    # Se usuário deseja consultar resultado por data
    if resposta == "3":
        limpar_terminal()
        # Solicita data no formato DD/MM/AAAA
        
        
        while True:
            data_desejada_string = input("\nDigite a data que deseja buscar suas informações de sustentabilidade!! (DD/MM/AAAA): ")
            
            if( not data_desejada_string):
                print("Digite uma data correta...")
            else:
                break
        
        try:
            # Converte string para objeto datetime.date
            data_desejada = datetime.strptime(data_desejada_string, "%d/%m/%Y").date()
            
            # Conecta ao banco e cria cursor para consultas
            conexao = conectar()
            cursor = conexao.cursor(dictionary=True)
            
            # Consulta no banco os dados do usuário para a data informada
            comando = """
                SELECT data_resposta, pontuacao, respostas, id_desafio, valor 
                FROM respostas_desafios 
                WHERE id_usuario = %s AND data_resposta = %s 
                ORDER BY data_resposta DESC
            """
            cursor.execute(comando, (usuario_logado["id"], data_desejada))
            dados = cursor.fetchall()
            
            # Inicializa console do rich para impressão formatada
            console = Console()
            
            # Verifica se encontrou dados
            if dados:
                # Cria tabela com título e colunas
                t = Table(title="\nHistórico de Sustentabilidade")
                t.add_column("N° DESAFIO", justify="left", style="white")
                t.add_column("RESPOSTA", justify="center", style="white")
                t.add_column("PONTUAÇÃO", justify="left", style="white")
                t.add_column("VALOR FORNECIDO", justify="center", style="white")
                t.add_column("DATA", justify="center", style="white")
                
                # Adiciona cada linha de dados na tabela
                for linha in dados:
                    desafio = str(linha['id_desafio'])
                    resposta = str(linha['respostas'])
                    valor = str(linha['valor'])
                    pontuacao = str(linha['pontuacao'])
                    # Formata a data para exibição legível
                    data_formatada = linha['data_resposta'].strftime('%d/%m/%Y %H:%M')
                    t.add_row(desafio, resposta, pontuacao, valor, data_formatada)
                
                # Exibe a tabela no console
                console.print(t)
            
            else:
                # Caso não existam registros para essa data
                print(f"\nNenhum desafio foi respondido em {data_desejada.strftime('%d/%m/%Y')}.")
        
        except ValueError:
            # Caso o formato da data seja inválido
            print("Formato de data inválido. Use o formato DD/MM/AAAA.")
    
    # Loop para alteração dos valores fornecidos pelo usuário em cada desafio
    while True:
        print("\nPara alterar o valor que você forneceu em cada desafio, basta digitar o número correspondente ao desafio (1 para Água / 2 para Resíduos ...)")
        print("Para voltar ao MENU digite 5...")
        alter_desa = input("Digite o que deseja: ")
        
        # Se usuário deseja voltar ao menu, sai do loop
        if alter_desa == "5":
            limpar_terminal()
            Tela_menu(usuario_logado)
            break
        
        # Conecta ao banco e cria cursor
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        
        # Comando SQL para atualizar as respostas do usuário
        comando = "UPDATE respostas_desafios SET valor = %s, respostas = %s, pontuacao = %s WHERE id_usuario = %s AND id_desafio = %s"
        
        # Alteração para desafio RESÍDUOS
        if alter_desa == "2":
            # Solicita peso do lixo reciclável e não reciclável
            consumoresiduos1 = float(input("Quanto pesa seu lixo reciclável em gramas(g)? "))
            consumoresiduos2 = float(input("Quanto pesa seu lixo não reciclável em gramas(g)? "))
            
            # Avalia sustentabilidade com base nas proporções
            if consumoresiduos1 > consumoresiduos2 * 1.5:
                residuos = "ALTA SUSTENTABILIDADE"
                pontos2 = 10
            elif consumoresiduos1 >= consumoresiduos2 * 1.2:
                residuos = "MODERADA SUSTENTABILIDADE"
                pontos2 = 5
            else:
                residuos = "BAIXA SUSTENTABILIDADE"
                pontos2 = 2
            
            # Atualiza os dados no banco
            cursor.execute(comando, (consumoresiduos1, residuos, pontos2, usuario_logado["id"], alter_desa))
            conexao.commit()
        
        # Alteração para desafio ÁGUA
        elif alter_desa == "1":
            consumoagua = float(input("Qual o seu consumo de água em metros cúbicos (m³)? "))
            consumoagua1 = consumoagua * 1000  # Converte para litros
            
            if consumoagua1 < 150:
                agua = "ALTA SUSTENTABILIDADE"
                pontos1 = 10
            elif 150 <= consumoagua1 <= 200:
                agua = "MODERADA SUSTENTABILIDADE"
                pontos1 = 5
            else:
                agua = "BAIXA SUSTENTABILIDADE"
                pontos1 = 2
            
            cursor.execute(comando, (consumoagua1, agua, pontos1, usuario_logado["id"], alter_desa))
            conexao.commit()
        
        # Alteração para desafio ENERGIA
        elif alter_desa == "3":
            kwh = int(input("Digite quanto você gasta de energia em Kwh: "))
            
            if kwh < 5:
                energia = "ALTA SUSTENTABILIDADE"
                pontos3 = 10
            elif 5 <= kwh <= 10:
                energia = "MODERADA SUSTENTABILIDADE"
                pontos3 = 5
            else:
                energia = "BAIXA SUSTENTABILIDADE"
                pontos3 = 2
            
            cursor.execute(comando, (kwh, energia, pontos3, usuario_logado["id"], alter_desa))
            conexao.commit()
        
        # Alteração para desafio TRANSPORTE
        elif alter_desa == "4":
            print("\nPARA ATUALIZAR SELECIONE UMA OPÇÃO\n")
            print("1 - Sem gasto de combustíveis fósseis (a pé, bicicleta, patinete ou outro meio)")
            print("2 - Uso misto de transporte público e privado (ônibus, carona ou outro meio)")
            print("3 - Uso exclusivo e privado (veículo próprio)")
            escolha = input("Digite a opção: ")
            
            if escolha == "1":
                transporte = "SEM GASTO DE COMBUSTÍVEIS FÓSSEIS"
                pontos4 = 10
            elif escolha == "2":
                transporte = "USO MISTO DE TRANSPORTE PÚBLICO E PRIVADO"
                pontos4 = 5
            elif escolha == "3":
                transporte = "USO EXCLUSIVO E PRIVADO"
                pontos4 = 2
            else:
                print("Opção inválida.")
                continue
            
            cursor.execute(comando, (transporte, transporte, pontos4, usuario_logado["id"], alter_desa))
