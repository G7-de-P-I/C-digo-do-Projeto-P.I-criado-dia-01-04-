import os
from banco import conectar
from datetime import datetime


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def Tela_desafio(usuario_logado):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT d.id, d.nome, COALESCE(r.status, 'NÃO CONCLUÍDO') AS status
        FROM desafios d
        LEFT JOIN respostas_desafios r
            ON d.id = r.id_desafio AND r.id_usuario = %s
        ORDER BY d.id
    """

    cursor.execute(query, (usuario_logado['id'],))
    desafios = cursor.fetchall()

    todos_concluidos = all(desafio['status'].upper() == "CONCLUIDO" for desafio in desafios)

    if todos_concluidos:
        print("\n✅ Você já concluiu todos os desafios!")
        input("Pressione ENTER para continuar...")
        Tela_opcoes(usuario_logado)
    else:
        print("\nDesafios disponíveis:")
        for desafio in desafios:
            print(f"{desafio['nome']}: {desafio['status'].upper()}")

        input("\nPressione ENTER para começar os desafios...")
        Tela_agua(usuario_logado)       
        
        
        
# Função para a tela do desafio água     
def Tela_agua(usuario_logado):
    from tela_menu import Tela_menu
    data_agora = datetime.now()

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
        Salvar_no_Banco(usuario_logado, 1, agua, pontos1, "Concluido", data_agora )
        print("Seu nível no DESAFIO 1 - ÁGUA é: ALTA SUSTENTABILIDADE")
        
    elif 150 <= consumoagua1 <= 200:
        agua = "MODERADA SUSTENTABILIDADE"
        pontos1 = 5
        # Salva os dados no banco de dados
        Salvar_no_Banco(usuario_logado, 1, agua, pontos1, "Concluido", data_agora )
        print("Seu nível no DESAFIO 1 - ÁGUA é: MODERADA SUSTENTABILIDADE")
        
    else:
        agua = "BAIXA SUSTENTABILIDADE"
        pontos1 = 2
        # Salva os dados no banco de dados
        Salvar_no_Banco(usuario_logado, 1, agua, pontos1, "Concluido", data_agora )
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
        data_agora = datetime.now()
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
            Salvar_no_Banco(usuario_logado, 2, residuos, pontos2, "Concluido", data_agora )
            print("Seu nível no DESAFIO 2 - RESÍDUOS é: ALTA SUSTENTABILIDADE")
    
        elif ((consumoresiduos1>=consumoresiduos2*1.2) and (consumoresiduos1<=consumoresiduos2*1.5)):
            residuos = "MODERADA SUSTENTABILIDADE"
            pontos2 = 5
            # Salva os dados no banco de dados
            Salvar_no_Banco(usuario_logado, 2, residuos, pontos2, "Concluido", data_agora )
            print("Seu nível no DESAFIO 2 - RESÍDUOS é: MODERADA SUSTENTABILIDADE")
        elif (consumoresiduos1<consumoresiduos2*0.8):
            residuos = "BAIXA SUSTENTABILIDADE"
            pontos2 = 2
            # Salva os dados no banco de dados
            Salvar_no_Banco(usuario_logado, 2, residuos, pontos2, "Concluido", data_agora )
            print("Seu nível no DESAFIO 2 - RESÍDUOS é: BAIXA SUSTENTABILIDADE")
        else:
            residuos = "BAIXA SUSTENTABILIDADE"
            pontos2 = 2
            # Salva os dados no banco de dados
            Salvar_no_Banco(usuario_logado, 2, residuos, pontos2, "Concluido", data_agora )
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
            data_agora = datetime.now()

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
                Salvar_no_Banco(usuario_logado, 3, energia, pontos3, "Concluido", data_agora )
                print("Seu nível no DESAFIO 3 - ENERGIA É: ALTA SUSTENTABILIDADE")
             
            elif 5 <= kwh <= 10:
                energia = "MODERADA SUSTENTABILIDADE"
                pontos3 = 5
                # Salva os dados no banco de dados
                Salvar_no_Banco(usuario_logado, 3, energia, pontos3, "Concluido", data_agora )
                print("Seu nível no DESAFIO 3 - ENERGIA É: MODERADA SUSTENTABILIDADE")
             
            else:
                energia = "BAIXA SUSTENTABILIDADE"
                pontos3 = 2
                # Salva os dados no banco de dados
                Salvar_no_Banco(usuario_logado, 3, energia, pontos3, "Concluido", data_agora )
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
    data_agora = datetime.now()

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
                transporte = "Sem gasto de combustíveis fósseis"
                pontos4 = 10
                print("Seu nível no DESAFIO 4 - TRANSPORTE É: ALTA SUSTENTABILIDADE")

            elif meiotransporte == 2:
                transporte = "Uso misto de transporte público e privado"
                pontos4 = 5
                print("Seu nível no DESAFIO 4 - TRANSPORTE É: MODERADA SUSTENTABILIDADE")

            elif meiotransporte == 3:
                transporte = "Uso exclusivo e privado"
                pontos4 = 2
                print("Seu nível no DESAFIO 4 - TRANSPORTE É: BAIXA SUSTENTABILIDADE\n")

            else:
                print("Digite uma opção válida (1, 2 ou 3).\n")
                continue  # volta pro início do loop

            # Se chegou aqui, é porque a opção foi válida
            # Salva no banco de dados
            Salvar_no_Banco(usuario_logado, 4, transporte, pontos4, "Concluido", data_agora)
            break

        except ValueError:
            print("\nErro: Digite um número válido.\n")
                
    # Limpa o terminal e chama a tela de opções
    limpar_terminal()
    print("\nMUITO BEM, DESAFIOS TERMINADOS\n")
    Tela_opcoes(usuario_logado)
        
    
            

def Tela_opcoes(usuario_logado):
    from tela_historico import Tela_historico
    print("")
    print("----------------------------------------------------------------------")
            # Nível de sustentabilidade para transporte
                
     
    print("--------------------------------------------------------------------")
    print("\nDESAFIOS CONCLUÍDOS\n")
    print("Escolha uma opção:")
    print("1 - LEVANTAMENTO DE DADOS")
    print("2 - SUSTENTABILIDADE MENSAIS")
    print("3 - SUSTENTABILIDADE DIÁRIA")
    print("4 - VER TABELA DE SUSTENTABILIDADE")
    print("5 - VOLTAR PARA A TELA DE MENU")
            
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
            

def Salvar_no_Banco(usuario_logado, id_desafio, resposta, pontuacao, status, data_resposta ):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
    
    
        comando = "INSERT INTO respostas_desafios(id_usuario, id_desafio, respostas, pontuacao, status, data_resposta) VALUES(%s, %s, %s, %s, %s, %s)"
        valores = (usuario_logado['id'], id_desafio, resposta, pontuacao, status, data_resposta)
    
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
            

# Função para a tela de sustentabilidade mensal      
def Tela_mensal(usuario_logado):
    from datetime import date


    print("----------------------------------------------------------------------")
    print("SUSTENTABILIDADE MENSAL")
    print("----------------------------------------------------------------------\n")

 # Conectar ao banco
    conexao = conectar()
    cursor = conexao.cursor()
    id_usuario = usuario_logado["id"]

    # Verificar quantos registros mensais já existem para esse usuário
    comando_verificar = """
    SELECT COUNT(*) FROM resultados_desafios
    WHERE id_usuario = %s
    """
    cursor.execute(comando_verificar, (id_usuario,))
    quantidade_registros = cursor.fetchone()[0]

    # Selecionar as pontuações diárias
    comando_pontuacoes = "SELECT pontuacao FROM respostas_desafios WHERE id_usuario = %s"
    cursor.execute(comando_pontuacoes, (id_usuario,))
    resultado = cursor.fetchall()

    # Lista com os pontos dos 30 dias
    desafios_diarios = [sum(linha) for linha in resultado]

    # Só continua se tiver 30 respostas
    if len(desafios_diarios) >= 30 and quantidade_registros == 0:
        # Calcular média mensal
            Smensal = sum(desafios_diarios) / 30

    # Mostrar nível (opcional)
            if 30 <= Smensal <= 40:
                nivel = "ALTA"
            elif 20 <= Smensal < 30:
                nivel = "MODERADA"
            else:
                nivel = "BAIXA"

            print(f"Sua média de pontos mensal foi: {Smensal:.2f}")
            print(f"NÍVEL DE SUSTENTABILIDADE MENSAL: {nivel}!\n")

    # Inserir na tabela de resultados mensais
            comando_inserir = """
            INSERT INTO resultados_desafios (id_usuario, resultado_mensal, data)
            VALUES (%s, %s, %s)
            """
            data_atual = date.today()
            cursor.execute(comando_inserir, (id_usuario, Smensal, data_atual))
            conexao.commit()
    else:
            print("Ainda não há 30 dias de resultados ou já foi registrado um resultado mensal.")

    # Fechar conexão
    cursor.close()
    conexao.close()

    # Menu de opções
    while True:
        print("----------------------------------------------------------------------")
        print("Escolha uma opção:")
        print("1 - MENU DE OPÇÕES")
        print("2 - Sair")
        print("----------------------------------------------------------------------")
        opcao = input("Digite a opção desejada: ")


        if opcao == "1":
            limpar_terminal()
            Tela_opcoes(usuario_logado)
            break

        elif opcao == "2":
            limpar_terminal()
            print("\nAté mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            

#------------------------------------

def Tela_dia(usuario_logado, pontos1, pontos2, pontos3, pontos4):
    from tela_principal import Tela_de_dicas
    from tela_principal import Tela_principal
    from tela_principal import Tela_de_saida
     
    while True:
        print("----------------------------------------------------------------------")
        print("\nPARABÉNS, VOCÊ CONCLUIU O DESAFIO SUSTENTAÍ!\n")
        print("\nAgora você poderá saber o quão sustentável você é!\n")
     
        variavel_do_nivel=(pontos1+pontos2+pontos3+pontos4)
        
        if (variavel_do_nivel>=30) and (variavel_do_nivel<=40):
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É: ALTO!")
            print("----------------------------------------------------------------------")
            
        elif (variavel_do_nivel>=20) and (variavel_do_nivel<=29):
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É MODERADO!")
            print("----------------------------------------------------------------------")
            
        else:
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É BAIXO!")
            print("----------------------------------------------------------------------")
            print("")
            print("Mas fique tranquilo(a), vamos te ajudar a melhorar...")
            
        print("\nEscolha uma opção:")
        print("1 - MENU OPÇÕES")
        print("2 - OBTER DICAS")
        print("3 - MENU PRINCIPAL")
        print("4 - SAIR")
        
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            limpar_terminal()
            Tela_opcoes(usuario_logado)  
            
        elif opcao == 2:
            limpar_terminal()
            Tela_de_dicas()
    
        elif opcao == 3: 
            limpar_terminal()
            Tela_principal(usuario_logado)
            
        elif opcao == 4:
            limpar_terminal()
            Tela_de_saida(usuario_logado)
            
            break
        else:
            print("\nOpção inválida! Digite uma opção válida!")
            
            
            
            
            
def Tela_dados(usuario_logado, pontos1, pontos2, pontos3, pontos4):
        from tela_principal import Tela_de_dicas
        from tela_principal import Tela_de_saida
        
        conexao = conectar()
        cursor = conexao.cursor()
    
        comando = "SELECT pontuacao FROM respostas_desafios WHERE id_usuario = %s"
    
        cursor.execute(comando, (usuario_logado["id"],))
        resultado = cursor.fetchall()
    
        cursor.close()
        conexao.close()

        
        desafios_diarios = [sum(linha) for linha in resultado]
        
        total_pontos = pontos1 + pontos2 + pontos3 + pontos4 
        if total_pontos > 0:
            porcentagem1 = (pontos1 / total_pontos) * 100
            porcentagem2 = (pontos2 / total_pontos) * 100
            porcentagem3 = (pontos3 / total_pontos) * 100
            porcentagem4 = (pontos4 / total_pontos) * 100
        else:
            porcentagem1 = porcentagem2 = porcentagem3 = porcentagem4 = 0
            
        print("----------------------------------------------------------------------")
        print(" ")
        print("LEVANTAMENTO DE DADOS DIÁRIO")
        print("----------------------------------------------------------------------")
        print(" ")
        print("")
        print("Vamos ver detalhes da sua performance diária...")
        print("\nAgora você poderá saber o quão sustentável você é e onde pode melhorar, caso necessário!")
        print("Nível de sustentabilidade (diário) de acordo com cada desafio: ")
        print(" ")
        print(f"\nDesafio 1: {pontos1} pontos")
        print(f"\nDesafio 2: {pontos2} pontos")
        print(f"\nDesafio 3: {pontos3} pontos")
        print(f"\nDesafio 4: {pontos4} pontos")
        print(" ")
        print("\nDistribuição percentual dos pontos:")
        print(" ")
        print(f"\nDesafio 1: {porcentagem1:.2f}%")
        print(f"\nDesafio 2: {porcentagem2:.2f}%")
        print(f"\nDesafio 3: {porcentagem3:.2f}%")
        print(f"\nDesafio 4: {porcentagem4:.2f}%")
        print(" ")
        
        while True:
            print("\nEscolha uma opção:")
            print("1 - MENU OPCÕES")
            print("2 - DICAS")
            print("3 - Sair")
            opcao9 = int(input("\nDigite a opção desejada: "))
        
            if opcao9 == 1:
                limpar_terminal()
                Tela_opcoes(usuario_logado)
            
            elif opcao9==2:
                limpar_terminal()
                Tela_de_dicas(usuario_logado)
            
            elif opcao9==3:
                print("\nVocê encerrou o programa. Até mais!")
                limpar_terminal()
                Tela_de_saida()
            
            else:
                print("\nOpção inválida! Tente novamente.")

