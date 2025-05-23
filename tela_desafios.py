import os
from banco import conectar
from datetime import date
from colorama import Fore, Style 


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def Tela_desafio(usuario_logado):
    data_hoje = date.today().isoformat()
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    query = """
    SELECT 1 FROM respostas_desafios
    WHERE id_usuario = %s AND data_resposta = %s
    LIMIT 1
    """

    cursor.execute(query, (usuario_logado['id'], data_hoje))
    desafios = cursor.fetchall()

    

    if desafios:
        print(Fore.GREEN+"\n✅ Você já concluiu todos os desafios!"+Style.RESET_ALL)
        input("Pressione ENTER para continuar...")
        Tela_opcoes(usuario_logado)
    else:
        print("\nDesafios disponíveis:")
        print("")
        print("1 - DESAFIO ÁGUA")
        print("2 - DESAFIO RESÍDUOS")
        print("3 - DESAFIO ENERGIA")
        print("4 - DESAFIO TRANSPORTE")
        
        input("\nPressione ENTER para começar os desafios...")
        Tela_agua(usuario_logado)       
        
        
        
# Função para a tela do desafio água     
def Tela_agua(usuario_logado):
    from tela_menu import Tela_menu
    data_agora = date.today().isoformat()

    # Explicação do desafio água
    print("----------------------------------------------------------------------")
    print("DESAFIO 1 - ÁGUA:")
    print("----------------------------------------------------------------------")
    print("")
    print(f"Agora que te conhecemos bem {usuario_logado['nome']}, esperamos que nos ajude a realizar nosso desafio nº1!")
    print("")
    print("Como medir seu consumo:")
    print("")
    print("1- Encontre o hidrômetro - Normalmente, ele fica na parte externa da casa, na garagem ou no jardim.")
    print("2- Anote os números - Veja os números pretos no visor do hidrômetro. Eles indicam o consumo total em metros cúbicos (m³).")
    print("3- Faça o valor dividido por 30 (valor/30) se for sua primeira vez no desafio.")
    print("")

    # Pede para o usuário digitar o valor do seu consumo de água e verifica se um valor válido foi digitado
    while True:
        try:
            print("")
            consumoagua = float(input("Qual o seu consumo de água em metros cúbicos (m³)? "))
            break
        except ValueError:
            print("")
            print("Erro: Digite um valor numérico válido para o consumo de água.")
            print("")
            print("----------------------------------------------------------------------")
    
    consumoagua1 = consumoagua * 1000  # Convertendo o consumo para litros
    
    # Determinando a sustentabilidade
    if consumoagua1 < 150:
        agua = "ALTA SUSTENTABILIDADE"
        pontos1 = 10
        # Salva os dados no banco de dados
        Salvar_no_Banco(usuario_logado, 1, agua, pontos1, "Concluido", data_agora, consumoagua1 )
        print("Seu nível no DESAFIO 1 - ÁGUA é: ALTA SUSTENTABILIDADE")
        
    elif 150 <= consumoagua1 <= 200:
        agua = "MODERADA SUSTENTABILIDADE"
        pontos1 = 5
        # Salva os dados no banco de dados
        Salvar_no_Banco(usuario_logado, 1, agua, pontos1, "Concluido", data_agora, consumoagua1 )
        print("Seu nível no DESAFIO 1 - ÁGUA é: MODERADA SUSTENTABILIDADE")
        
    else:
        agua = "BAIXA SUSTENTABILIDADE"
        pontos1 = 2
        # Salva os dados no banco de dados
        Salvar_no_Banco(usuario_logado, 1, agua, pontos1, "Concluido", data_agora, consumoagua1 )
        print("Seu nível no DESAFIO 1 - ÁGUA é: BAIXA SUSTENTABILIDADE")
    
    # Opção de continuar para o próximo desafio ou voltar para a tela de menu
    print("----------------------------------------------------------------------")
    print("")
    print("Escolha uma opção:")
    print("1 - CONTINUAR")
    print("2 - VOLTAR PARA A TELA MENU")
    
    # Pede para o usuário digitar a opção escolhida e verifica se um valor válido foi digitado
    while True:
        try:
            print("")
            opcao1 = int(input("Digite a opção escolhida: "))
            if opcao1 not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Erro: Digite um valor numérico válido para opção.")
    
    print("")


    if opcao1 == 2:
        # Limpa o terminal e chama a tela de menu
        limpar_terminal()
        Tela_menu(usuario_logado)
    
    elif opcao1 == 1:
        # Limpa o terminal e chama a tela do desafio resìduos
        limpar_terminal()
        Tela_residuos(usuario_logado)

# Função para a tela do desafio resíduos
def Tela_residuos(usuario_logado):
        from tela_menu import Tela_menu
        data_agora = date.today().isoformat()
        limpar_terminal()

        # Tela de explicação do desafio resíduos
        print("----------------------------------------------------------------------")
        print("DESAFIO 2 - RESÍDUOS:")
        print("----------------------------------------------------------------------")
        print("")
        print("DESAFIO RESÍDUOS PARTE 1")
        print("")
        print("Para concluir esse desafio, pense nas embalagens recicláveis e não recicláveis: ")
        print("")
        print("Como medir seu consumo de resíduos:")
        print("")
        print("1- Separe os resíduos - Divida seu lixo em dois sacos: ")
        print("\tRECICLÁVEIS: Plásticos, papéis, vidros e metais limpos.")
        print("\tNÃO RECICLÁVEIS: Restos de comida, papel higiênico, embalagens sujas, etc." )
        print("2- Pese os sacos - Use uma balança doméstica para medir o peso de cada tipo de resíduo")
        print("3- Registre os valores - Anote a quantidade (peso) de lixo reciclável e não reciclável que você produz em um dia. ")
        
        # Pede para o usuário digitar o peso do seu consumo de lixo reciclável e verifica se um valor válido foi digitado
        while True:
            try:
                print("")
                consumoresiduos1=float(input("Quanto pesa seu lixo reciclável em gramas(g)? "))
                break
            except ValueError:
                print("")
                print("Erro: Digite um valor númerico válido para resíduo.")

        # Opção de continuar para a parte 2 do desafio resíduos ou voltar para a tela de menu
        print("")
        print("Escolha uma opção:")
        print("")
        print("1 - CONTINUAR PARA DESAFIO RESÍDUOS PARTE 2")
        print("2 - VOLTAR PARA A TELA MENU")
        
        print("")

        # Pede para o usuário digitar a opção escolhida e verifica se um valor válido foi digitado
        while True:
            try:
                opcao3=int(input("Digite a opção escolhida: "))
                break
            except ValueError:
                print("")
                print("Erro: Digite um valor númerico válido para opção.")
                print("")
                
        if opcao3 == 2:
            # Limpa o terminal e chama a tela de menu
            limpar_terminal()
            Tela_menu(usuario_logado)

        elif (opcao3==1):
            # Limpa o terminal e abre a parte 2 do desafio resíduos
            limpar_terminal()

            # Explica a parte 2 do desafio resíduos
            print("----------------------------------------------------------------------")
            print("DESAFIO RESÍDUOS PARTE 2")
            print("----------------------------------------------------------------------")
            print("")
            print("Para concluir esse desafio, pense nas embalagens recicláveis e não recicláveis: ")
            print("")
            print("Como medir seu consumo de resíduos:")
            print("")
            print("1- Separe os resíduos - Divida seu lixo em dois sacos: ")
            print("\tRECICLÁVEIS: Plásticos, papéis, vidros e metais limpos.")
            print("\tNÃO RECICLÁVEIS: Restos de comida, papel higiênico, embalagens sujas, etc." )
            print("2- Pese os sacos - Use uma balança doméstica para medir o peso de cada tipo de resíduo")
            print("3- Registre os valores - Anote a quantidade (peso) de lixo reciclável e não reciclável que você produz em um dia. ")
        
           # Pede para o usuario digitar o peso do seu consumo de lixo não reciclável e verifica se um valor válido foi digitado
        while True:
                try:
                    print("")
                    consumoresiduos2=float(input("Quanto pesa seu lixo não reciclável em gramas(g)? "))
                    break
                except ValueError:
                    print("")
                    print("Erro: Digite um valor númerico válido para resíduo.")
        print("")
        print("----------------------------------------------------------------------") 
        
        # Determina a sustentabilidade do desafio resíduos
        if (consumoresiduos1>consumoresiduos2*1.5):
            residuos = "ALTA SUSTENTABILIDADE"
            pontos2 = 10
            # Salva os dados no banco de dados
            Salvar_no_Banco(usuario_logado, 2, residuos, pontos2, "Concluido", data_agora, consumoresiduos1 )
            print("Seu nível no DESAFIO 2 - RESÍDUOS é: ALTA SUSTENTABILIDADE")
    

        elif ((consumoresiduos1>=consumoresiduos2*1.2) and (consumoresiduos1<=consumoresiduos2*1.5)):
            residuos = "MODERADA SUSTENTABILIDADE"
            pontos2 = 5
            # Salva os dados no banco de dados
            Salvar_no_Banco(usuario_logado, 2, residuos, pontos2, "Concluido", data_agora, consumoresiduos1 )
            print("Seu nível no DESAFIO 2 - RESÍDUOS é: MODERADA SUSTENTABILIDADE")
        elif (consumoresiduos1<consumoresiduos2*0.8):
            residuos = "BAIXA SUSTENTABILIDADE"
            pontos2 = 2
            # Salva os dados no banco de dados
            Salvar_no_Banco(usuario_logado, 2, residuos, pontos2, "Concluido", data_agora, consumoresiduos1 )
            print("Seu nível no DESAFIO 2 - RESÍDUOS é: BAIXA SUSTENTABILIDADE")
        else:
            residuos = "BAIXA SUSTENTABILIDADE"
            pontos2 = 2
            # Salva os dados no banco de dados
            Salvar_no_Banco(usuario_logado, 2, residuos, pontos2, "Concluido", data_agora, consumoresiduos1 )
            print("Seu nível no DESAFIO 2 - RESÍDUOS é: BAIXA SUSTENTABILIDADE")
    
        # Opção de continuar para o próximo desafio ou voltar para a tela de menu
        print("----------------------------------------------------------------------")
        print("")     
        print("Escolha uma opção:")
        print("1 - CONTINUAR")
        print("2 - VOLTAR PARA A TELA MENU")
    
        # Pede para o usuário digitar a opção escolhida e verifica se um valor válido foi digitado
        while True:
            try:
                print("")
                opcao4=int(input("Digite a opção escolhida: "))
                break
            except ValueError:
                print("")
                print("Erro: Digite um valor númerico válido para opção.")
            
        print("")   
    
        if opcao4 == 2:
            # Limpa o terminal e chama a tela de menu
            limpar_terminal()
            Tela_menu(usuario_logado)
    
        elif (opcao4==1):
            # Limpa o terminal e chama a tela do desafio energia
            limpar_terminal()
            Tela_energia(usuario_logado)

        
# Função para a tela do desafio energia      
def Tela_energia(usuario_logado):
            from tela_menu import Tela_menu
            data_agora = date.today().isoformat()

            # Tela de explicação do desafio energia
            print("----------------------------------------------------------------------") 
            print("DESAFIO 3 - ENERGIA")
            print("----------------------------------------------------------------------") 
            print("\nQuase lá! Estamos perto de saber seu nível de sustentabilidade! Saber seu consumo de energia é essencial para completar o desafio.")
            print("")
            print("Como verificar seu consumo:")
            print("\n1. Pegue sua conta de energia -")
            print("Encontre a fatura referente ao mês atual.")
            print("\n2. Localize o consumo mensal -")
            print("Procure a informação de consumo total, geralmente expressa em kWh (quilowatt-hora).")
         
            # Pede para o usuário digitar o seu consumo de energia e verifica se um valor válido foi digitado
            while True:
                try:
                    print("")
                    kwh = int(input("Digite quanto você gasta de energia em Kwh: "))
                    break
                except ValueError:
                    print("")
                    print("Erro: Digite um valor numérico válido para o consumo de energia.")
     
            print("")
            print("----------------------------------------------------------------------")
         
            # Determina a sustentabilidade do desafio energia
            if kwh < 5:
                energia = "ALTA SUSTENTABILIDADE"
                pontos3 = 10
                # Salva os dados no banco de dados
                Salvar_no_Banco(usuario_logado, 3, energia, pontos3, "Concluido", data_agora, kwh)
                print("Seu nível no DESAFIO 3 - ENERGIA É: ALTA SUSTENTABILIDADE")
             
            elif 5 <= kwh <= 10:
                energia = "MODERADA SUSTENTABILIDADE"
                pontos3 = 5
                # Salva os dados no banco de dados
                Salvar_no_Banco(usuario_logado, 3, energia, pontos3, "Concluido", data_agora, kwh)
                print("Seu nível no DESAFIO 3 - ENERGIA É: MODERADA SUSTENTABILIDADE")
             
            else:
                energia = "BAIXA SUSTENTABILIDADE"
                pontos3 = 2
                # Salva os dados no banco de dados
                Salvar_no_Banco(usuario_logado, 3, energia, pontos3, "Concluido", data_agora, kwh)
                print("Seu nível no DESAFIO 3 - ENERGIA É: BAIXA SUSTENTABILIDADE")
     
            # Opção de continuar para o próximo desafio ou voltar para a tela de menu
            print("----------------------------------------------------------------------") 
            print("")
            print("Escolha uma opção:")
            print("")
            print("1 - CONTINUAR")
            print("2 - VOLTAR PARA A TELA MENU")
         
            # Pede para o usuário digitar a opção escolhida e verifica se um valor válido foi digitado
            while True:
                try:
                    print("")
                    opcao8 = int(input("Digite a opção escolhida: "))
                    break
                except ValueError:
                    print("")
                    print("Erro: Digite uma opção válida.")
     
            print("")

            if opcao8 == 2:
                # Limpa o terminal e chama a tela de menu
                limpar_terminal()
                Tela_menu(usuario_logado)
         
            elif opcao8 == 1:
                # Limpa o terminal e chama a tela do desafio transporte
                limpar_terminal()
                Tela_transporte(usuario_logado)
                
                
# Função para a tela desafio transporte            
def Tela_transporte(usuario_logado): 
    data_agora = date.today().isoformat()

    # Tela de explicação do desafio transporte
    print("----------------------------------------------------------------------")
    print("DESAFIO 4 - TRANSPORTE")
    print("----------------------------------------------------------------------")
    print("")
    print("Excelente! Você passou por quase todos os desafios, conclua o desafio 4 para descobrir o quão sustentável você é.")
    print("")
    print("Qual meio de transporte você mais utilizou hoje?")
    print("")
    print("Escolha uma opção:")
    print("")
    print("1 - Sem gasto de combustíveis fósseis (a pé, bicicleta, patinete ou outro meio)")
    print("2 - Uso misto de transporte público e privado (ônibus, carona ou outro meio)")
    print("3 - Uso exclusivo e privado (veículo próprio)")
    print("")
    
    # Pede para o usuário digitar o seu transporte mais utilizado no dia atual e verifica se um valor válido foi digitado
    while True:
        try:
            meiotransporte = int(input("Digite uma das opções: "))
        
            if meiotransporte == 1:
                transporte = "ALTA SUSTENTABILIDADE"
                pontos4 = 10
                print("Seu nível no DESAFIO 4 - TRANSPORTE É: ALTA SUSTENTABILIDADE")

            elif meiotransporte == 2:
                transporte = "MEDIA SUSTENTABILIDADE"
                pontos4 = 5
                print("Seu nível no DESAFIO 4 - TRANSPORTE É: MODERADA SUSTENTABILIDADE")

            elif meiotransporte == 3:
                transporte = "BAIXA SUSTENTABILIDADE"
                pontos4 = 2
                print("Seu nível no DESAFIO 4 - TRANSPORTE É: BAIXA SUSTENTABILIDADE\n")

            else:
                print("Digite uma opção válida (1, 2 ou 3).\n")
                continue  # volta pro início do loop

            # Se chegou aqui, é porque a opção foi válida
            # Salva no banco de dados
            Salvar_no_Banco(usuario_logado, 4, transporte, pontos4, "Concluido", data_agora, 0)
            break

        except ValueError:
            print("\nErro: Digite um número válido.\n")
                
    # Limpa o terminal e chama a tela de opções
    limpar_terminal()
    print("\nMUITO BEM, DESAFIOS TERMINADOS\n")
    Tela_opcoes(usuario_logado)
        
    
            

def Tela_opcoes(usuario_logado):
    from tela_historico import Tela_historico
    from tela_menu import Tela_menu
    from tela_mensal import Tela_mensal
    from tela_dados import Tela_dados
    from tela_dia import Tela_dia
    print("")
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
    print(Fore.BLUE+"MENU OPÇÕES"+Style.RESET_ALL)
            # Nível de sustentabilidade para transporte
    
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
    print("\nDESAFIOS CONCLUÍDOS\n")
    print("Escolha uma opção:")
    print("1 - LEVANTAMENTO DE DADOS")
    print("2 - SUSTENTABILIDADE MENSAIS")
    print("3 - SUSTENTABILIDADE DIÁRIA")
    print("4 - VER TABELA DE SUSTENTABILIDADE")
    print("5 - TELA DE MENU")
            
    conexao = conectar()
    cursor = conexao.cursor()
    
    comando = "SELECT pontuacao FROM respostas_desafios WHERE id_usuario = %s"
    
    cursor.execute(comando, (usuario_logado["id"],))
    resultado = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    desafios_diarios = [sum(linha) for linha in resultado] 
    
    while True:
        try:
            print("")
            opcao10 = int(input("Digite a opção escolhida: "))
            
        except ValueError:
            print("")
            print("Erro: Digite uma opção válida.")
            
        if(opcao10 == 1):
            limpar_terminal()
            Tela_dados(usuario_logado, desafios_diarios[0], desafios_diarios[1], desafios_diarios[2], desafios_diarios[3])
            break
        elif(opcao10 == 2):
            limpar_terminal()
            Tela_mensal(usuario_logado)
            break
        elif(opcao10 == 3):
            limpar_terminal()
            Tela_dia(usuario_logado, desafios_diarios[0], desafios_diarios[1], desafios_diarios[2], desafios_diarios[3])
            break
        elif(opcao10 == 4):
            limpar_terminal()
            Tela_historico(usuario_logado)
            break
        elif(opcao10 == 5):
            limpar_terminal()
            Tela_menu(usuario_logado)
            break
            

def Salvar_no_Banco(usuario_logado, id_desafio, resposta, pontuacao, status, data_resposta, valor ):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
    
    
        comando = "INSERT INTO respostas_desafios(id_usuario, id_desafio, respostas, pontuacao, status, data_resposta, valor) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        valores = (usuario_logado['id'], id_desafio, resposta, pontuacao, status, data_resposta, valor)
    
        cursor.execute(comando, valores)
        conexao.commit()
        print("✅ Resposta salva com sucesso!")
        
    except Exception as e:
        print(f"⚠️  Erro ao salvar resposta: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()