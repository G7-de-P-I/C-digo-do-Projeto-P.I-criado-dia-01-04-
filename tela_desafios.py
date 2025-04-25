import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

<<<<<<< Updated upstream
pontos1=10
pontos2=10
pontos3=10
pontos4=10

def Tela_desafio():
=======
def Tela_desafio(usuario_logado):
    from datetime import date
    
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    hoje = datetime.today()

    query = """ SELECT status FROM respostas_desafios WHERE id_usuario = %s AND DATE(data_resposta) = CURDATE()"""
    cursor.execute(query, (usuario_logado["id"],))
    resultado = cursor.fetchall()
    
    if resultado:
        print("\n✅ Você já concluiu todos os desafios de hoje!")
        input("Pressione ENTER para continuar...")
        Tela_opcoes(usuario_logado)
    else:
        print("\nDesafios disponíveis para hoje:")
        
        print("1 - DESAFIO ÁGUA")
        print("2 - DESAFIO RESÍDUOS")
        print("3 - DESAFIO ENERGIA")
        print("4 - DESAFIO TRANSPORTE")

        input("\nPressione ENTER para começar os desafios...")
        Tela_agua(usuario_logado)       
        
        
        
# Função para a tela do desafio água     
def Tela_agua(usuario_logado):
>>>>>>> Stashed changes
    from tela_menu import Tela_menu
    """cria uma tela de DESAFIOS."""
    print("----------------------------------------------------------------------")
    print("DESAFIOS")
    print("----------------------------------------------------------------------")
    print("")
    print("DESAFIO 1 - ÁGUA:        NÂO CONCLUIDO")
    print("DESAFIO 2 - RESÍDUOS:    NÃO CONCLUIDO")
    print("DESAFIO 3 - ENERGIA:     NÃO CONCLUIDO")
    print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
    print("")
    print("Escolha uma opção:")
    print("")
    print("1 - CONTINUAR PARA DESAFIO 1 - ÁGUA")
    print("2 - VOLTAR PARA A TELA MENU")

    while True:
        try:
            print("")
            opcao2=float(input("Digite a opção escolhida: ")) 
            break
        except ValueError:
            print("")
            print("Erro: Digite um valor númerico válido para opção.")
            
    print("")
            
    if opcao2 == 1:
        limpar_terminal()
        Tela_agua_residuos()
    
    elif opcao2 == 2:
        limpar_terminal()
        Tela_menu()


def Tela_desafio_energ():
     from tela_menu import Tela_menu
     desafio1 = 3
         
     # DESAFIO 3 - ENERGIA
     if desafio1 == 3:
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
         
         while True:
             try:
                 print("")
                 kwh = float(input("Digite quanto você gasta de energia em Kwh: "))
                 break
             except ValueError:
                 print("")
                 print("Erro: Digite um valor numérico válido para o consumo de energia.")
     
         print("")
         print("----------------------------------------------------------------------")
         
         # Nível de sustentabilidade para energia
         if kwh < 5:
             energia = "ALTA SUSTENTABILIDADE"
             pontos3 = 10
             print("Seu nível no DESAFIO 3 - ENERGIA É: ALTA SUSTENTABILIDADE")
             
         elif 5 <= kwh <= 10:
             energia = "MODERADA SUSTENTABILIDADE"
             pontos3 = 5
             print("Seu nível no DESAFIO 3 - ENERGIA É: MODERADA SUSTENTABILIDADE")
             
         else:
             energia = "BAIXA SUSTENTABILIDADE"
             pontos3 = 2
             print("Seu nível no DESAFIO 3 - ENERGIA É: BAIXA SUSTENTABILIDADE")
     
     # DESAFIO 4 - TRANSPORTE
     
     print("----------------------------------------------------------------------") 
     print("")
     print("Escolha uma opção:")
     print("")
     print("1 - CONTINUAR")
     print("2 - VOLTAR PARA A TELA MENU")
         
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
         limpar_terminal()
         Tela_menu()
         
     elif opcao8 == 1:
         limpar_terminal()
         print("----------------------------------------------------------------------")
         print("DESAFIOS")
         print("----------------------------------------------------------------------")
         print("") 
         print("DESAFIO 1 - ÁGUA:            CONCLUIDO")
         print("DESAFIO 2 - RESÍDUOS:        CONCLUIDO")
         print("DESAFIO 3 - ENERGIA:         CONCLUIDO")
         print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
         print("")
         print("Escolha uma opção:")
         print("1 - CONTINUAR PARA DESAFIO 4 - TRANSPORTE")
         print("2 - VOLTAR PARA A TELA DE MENU")
         
         while True:
             try:
                print("")
                desafio2 = int(input("Digite a opção escolhida: "))
                break
             except ValueError:
                print("")
                print("Erro: Digite uma opção numérica válida.")
     
         print("")
         
         if desafio2 == 1:
            limpar_terminal()
            Tela_desafio_transp()
             
         elif desafio2 == 2:
            limpar_terminal()
            Tela_menu()
  
def Tela_agua_residuos():
    from tela_menu import Tela_menu
    """criar uma tela agua"""
    print("----------------------------------------------------------------------")
    print("DESAFIO 1 - ÁGUA:")
    print("----------------------------------------------------------------------")
    print("")
    print("Agora que te conhecemos bem (nome), esperamos que nos ajude a realizar nosso desafio nº1!")
    print("")
    print("Como medir seu consumo:")
    print("")
    print("1- Encontre o hidrômetro - Normalmente, ele fica na parte externa da casa, na garagem ou no jardim.")
    print("2- Anote os números - Veja os números pretos no visor do hidrômetro. Eles indicam o consumo total em metros cúbicos (m*3)." )
    print("3- Faça o valor dividido por 30 (valor/30) se for sua primeita vez no desafio")
    print("")
    
    while True:
        try:
            print("")
            consumoagua=float(input("Qual o seu consumo de água em metros cúbicos (m*3)? "))
            break
        except ValueError:
            print("")
            print("Erro: Digite um valor númerico válido para o consumo de água.")
            print("")
            print("----------------------------------------------------------------------")
    consumoagua1=consumoagua*1000
    
    if (consumoagua1<150):
        agua = "ALTA SUSTENTABILIDADE"
        pontos1 = 10
<<<<<<< Updated upstream
        print("Seu nível no DESAFIO 1 - ÁGUA é: ALTA SUSTENTABILIDADE ")
=======
        # Salva os dados no banco de dados
        Salvar_no_Banco(usuario_logado, 1, agua, pontos1, "Concluido", data_agora, consumoagua )
        print("Seu nível no DESAFIO 1 - ÁGUA é: ALTA SUSTENTABILIDADE")
>>>>>>> Stashed changes
        
    elif ((consumoagua1>=150) and (consumoagua1<=200)):
        agua = "MODERADA SUSTENTABILIDADE"
        pontos1 = 5
<<<<<<< Updated upstream
        print("Seu nível no DESAFIO 1 - ÁGUA é: MODERADA SUSTENTABILIDADE ")
=======
        # Salva os dados no banco de dados
        Salvar_no_Banco(usuario_logado, 1, agua, pontos1, "Concluido", data_agora, consumoagua )
        print("Seu nível no DESAFIO 1 - ÁGUA é: MODERADA SUSTENTABILIDADE")
>>>>>>> Stashed changes
        
    else:
        agua = "BAIXA SUSTENTABILIDADE"
        pontos1 = 2
<<<<<<< Updated upstream
        print("Seu nível no DESAFIO 1 - ÁGUA é: BAIXA SUSTENTABILIDADE ")
    
=======
        # Salva os dados no banco de dados
        Salvar_no_Banco(usuario_logado, 1, agua, pontos1, "Concluido", data_agora, consumoagua )
        print("Seu nível no DESAFIO 1 - ÁGUA é: BAIXA SUSTENTABILIDADE")
>>>>>>> Stashed changes
    
    print("----------------------------------------------------------------------")
    print("")
    print("Escolha uma opção:")
    print("1 - CONTINUAR")
    print("2 - VOLTAR PARA A TELA MENU")    
    
    while True:
        try:
            print("")
            opcao1=float(input("Digite a opção escolhida: "))
            break
        except ValueError:
            print("")
            print("Erro: Digite um valor númerico válido para opção.")
            
    print("")
    
    if opcao1 == 2:
        limpar_terminal()
        Tela_menu()
    
    elif (opcao1==1):
        limpar_terminal()
        print("----------------------------------------------------------------------")
        print("DESAFIOS")
        print("----------------------------------------------------------------------")
        print("")
        print("DESAFIO 1 - ÁGUA:            CONCLUIDO")
        print("DESAFIO 2 - RESÍDUOS:    NÃO CONCLUIDO")
        print("DESAFIO 3 - ENERGIA:     NÃO CONCLUIDO")
        print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
        print("")
        print("Escolha uma opção:")
        print("")
        print("1 - CONTINUAR PARA DESAFIO 2 - RESÍDUOS")
        print("2 - VOLTAR PARA A TELA MENU")
        
        while True:
            try:
                print("")
                opcao2=float(input("Digite a opção escolhida: ")) 
                break
            except ValueError:
                print("")
                print("Erro: Digite um valor númerico válido para opção.")
    
    if (opcao1==2):
        limpar_terminal()
        Tela_menu()
        
    elif (opcao2==1):
        limpar_terminal()
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
        
        while True:
            try:
                print("")
                consumoresiduos1=float(input("Quanto pesa seu lixo reciclável em gramas(g)? "))
                break
            except ValueError:
                print("")
                print("Erro: Digite um valor númerico válido para resíduo.")
    
        print("")
        print("Escolha uma opção:")
        print("")
        print("1 - CONTINUAR PARA DESAFIO RESÍDUOS PARTE 2")
        print("2 - VOLTAR PARA A TELA MENU")
        
        print("")
        while True:
            try:
                opcao3=float(input("Digite a opção escolhida: "))
                break
            except ValueError:
                print("")
                print("Erro: Digite um valor númerico válido para opção.")
                print("")
                
    if opcao3 == 2:
        limpar_terminal()
        Tela_menu()
        
        
<<<<<<< Updated upstream
    elif (opcao3==1):
        limpar_terminal()
=======
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
>>>>>>> Stashed changes
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
    
    if (consumoresiduos1>consumoresiduos2*1.5):
        resíduos = "ALTA SUSTENTABILIDADE"
        pontos2 = 10
        print("Seu nível no DESAFIO 2 - RESÍDUOS é: ALTA SUSTENTABILIDADE")
    
<<<<<<< Updated upstream
    elif ((consumoresiduos1>=consumoresiduos2*1.2) and (consumoresiduos1<=consumoresiduos2*1.5)):
        resíduos = "MODERADA SUSTENTABILIDADE"
        pontos2 = 5
        print("Seu nível no DESAFIO 2 - RESÍDUOS é: MODERADA SUSTENTABILIDADE")
    elif (consumoresiduos1<consumoresiduos2*0.8):
        resíduos = "BAIXA SUSTENTABILIDADE"
        pontos2 = 2
        print("Seu nível no DESAFIO 2 - RESÍDUOS é: BAIXA SUSTENTABILIDADE")
    else:
        resíduos = "BAIXA SUSTENTABILIDADE"
        pontos2 = 2
        print("Seu nível no DESAFIO 2 - RESÍDUOS é: BAIXA SUSTENTABILIDADE")
    
    print("----------------------------------------------------------------------")
    print("")     
    print("Escolha uma opção:")
    print("1 - CONTINUAR")
    print("2 - VOLTAR PARA A TELA MENU")
    
=======
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
                Salvar_no_Banco(usuario_logado, 3, energia, pontos3, "Concluido", data_agora, kwh )
                print("Seu nível no DESAFIO 3 - ENERGIA É: ALTA SUSTENTABILIDADE")
             
            elif 5 <= kwh <= 10:
                energia = "MODERADA SUSTENTABILIDADE"
                pontos3 = 5
                # Salva os dados no banco de dados
                Salvar_no_Banco(usuario_logado, 3, energia, pontos3, "Concluido", data_agora, kwh )
                print("Seu nível no DESAFIO 3 - ENERGIA É: MODERADA SUSTENTABILIDADE")
             
            else:
                energia = "BAIXA SUSTENTABILIDADE"
                pontos3 = 2
                # Salva os dados no banco de dados
                Salvar_no_Banco(usuario_logado, 3, energia, pontos3, "Concluido", data_agora, kwh )
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
    desafios_diarios = [linha[0] if isinstance(linha, tuple) else linha['pontuacao'] for linha in resultado]

    
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
            

def Salvar_no_Banco(usuario_logado, id_desafio, resposta, pontuacao, status, data_resposta, valor):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
    
    
        comando = "INSERT INTO respostas_desafios(id_usuario, id_desafio, respostas, pontuacao, status, data_resposta, valor) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        valores = (usuario_logado['id'], id_desafio, resposta, pontuacao, status, data_resposta, valor )
    
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
    cursor = conexao.cursor(dictionary=True)
    id_usuario = usuario_logado["id"]

# Selecionar as pontuações diárias
    comando_pontuacoes = "SELECT pontuacao FROM respostas_desafios WHERE id_usuario = %s"
    cursor.execute(comando_pontuacoes, (id_usuario,))
    resultado = cursor.fetchall()

# Lista com os pontos
    desafios_diarios = [linha['pontuacao'] for linha in resultado]

    if desafios_diarios:
        Smensal = sum(desafios_diarios) / len(desafios_diarios)
        nivel = ""

        if 30 <= Smensal <= 40:
            nivel = "ALTA"
        elif 20 <= Smensal < 30:
            nivel = "MODERADA"
        else:
            nivel = "BAIXA"

        print(f"Sua média de pontos mensal foi: {Smensal:.2f}")
        print(f"NÍVEL DE SUSTENTABILIDADE MENSAL: {nivel}!\n")

    # Atualiza ou insere
        data_atual = date.today()
        verificar_existencia = """
            SELECT id FROM resultados_desafios
            WHERE id_usuario = %s AND MONTH(data) = MONTH(%s) AND YEAR(data) = YEAR(%s)
        """
        cursor.execute(verificar_existencia, (id_usuario, data_atual, data_atual))
        resultado_existente = cursor.fetchone()

        if resultado_existente:
            atualizar = """
                UPDATE resultados_desafios
                SET resultado_mensal = %s, data = %s
                WHERE id = %s
            """
            cursor.execute(atualizar, (nivel, data_atual, resultado_existente['id']))
        else:
            inserir = """
                INSERT INTO resultados_desafios (id_usuario, resultado_mensal, data)
                VALUES (%s, %s, %s)
            """
            cursor.execute(inserir, (id_usuario, nivel, data_atual))

    conexao.commit()

# Sempre feche a conexão
    cursor.close()
    conexao.close()
    

    # Menu de opções
>>>>>>> Stashed changes
    while True:
        try:
            print("")
            opcao4=float(input("Digite a opção escolhida: "))
            break
        except ValueError:
            print("")
            print("Erro: Digite um valor númerico válido para opção.")
            
    print("")   
    
    if opcao4 == 2:
        limpar_terminal()
        Tela_menu()
    
    elif (opcao4==1):
        limpar_terminal()
        print("----------------------------------------------------------------------") 
        print("DESAFIOS")
        print("----------------------------------------------------------------------") 
        print("")
        print("DESAFIO 1 - ÁGUA:            CONCLUIDO")
        print("DESAFIO 2 - RESÍDUOS:        CONCLUIDO")
        print("DESAFIO 3 - ENERGIA:     NÃO CONCLUIDO")
        print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
        print("")
        print("Escolha uma opção:")
        print("")
        print("1 - CONTINUAR PARA DESAFIO 3 - ENERGIA")
        print("2 - VOLTAR PARA A TELA MENU")
        print("")
            
        while True:
            try:
                print("")
                opcao5=float(input("Digite a opção escolhida: ")) 
                break
            except ValueError:
                print("")
                print("Erro: Digite um valor númerico válido para opção.")
                
        if opcao5 == 1:
                limpar_terminal()
                Tela_desafio_energ()
        
        elif opcao5 == 2:
                limpar_terminal()
                Tela_menu()        

    

def Tela_desafio_transp():
         from tela_menu import Tela_menu
         desafio2 = 1
         
         if desafio2 == 1:
             limpar_terminal()
             print("----------------------------------------------------------------------")
             print("DESAFIO 4 - TRANSPORTE")
             print("----------------------------------------------------------------------")
             print("")
             print("Excelente! Você passou por quase todos os desafios, conclua o desafio 4 para descobrir o quão sustentável você é.")
             print("")
             print("Qual meio de transporte você utilizou hoje?")
             print("")
             print("Escolha uma opção:")
             print("")
             print("1 - Sem gasto de combustíveis fósseis (a pé, bicicleta, patinete ou outro meio)")
             print("2 - Uso misto de transporte público e privado (ônibus, carona ou outro meio)")
             print("3 - Uso exclusivo e privado (trasnporte que utiliza combustíveis fósseis)")
             print("")
             
             
             
             while True:
                 try:
                     meiotransporte = int(input("Digite uma das opções: "))
                     break
                 except ValueError:
                     print("")
                     print("Erro: Digite um número válido.")
             
             print("")
             print("----------------------------------------------------------------------")
     
             # Nível de sustentabilidade para transporte
             if meiotransporte == 1:
                 transporte = "ALTA SUSTENTABILIDADE"
                 pontos4 = 10
                 print("Seu nível no DESAFIO 4 - TRANSPORTE É: ALTA SUSTENTABILIDADE")
                 
                 
                 
             elif meiotransporte == 2:
                 transporte = "MODERADA SUSTENTABILIDADE"
                 pontos4 = 5
                 print("Seu nível no DESAFIO 4 - TRANSPORTE É: MODERADA SUSTENTABILIDADE")
                 
             elif meiotransporte == 3:
                 transporte = "BAIXA SUSTENTABILIDADE"
                 pontos4 = 2
                 print("Seu nível no DESAFIO 4 - TRANSPORTE É: BAIXA SUSTENTABILIDADE")
                 
     
             print("--------------------------------------------------------------------")
             print("")
             print("Escolha uma opção:")
             print("1 - LEVANTAMENTO DE DADOS")
             print("2 - VOLTAR PARA A TELA DE MENU")
             
             while True:
                 try:
                     print("")
                     opcao10 = int(input("Digite a opção escolhida: "))
                     break
                 except ValueError:
                     print("")
                     print("Erro: Digite uma opção válida.")
            
             print("")
             
             
             if opcao10 == 1:
                 limpar_terminal()
                 Tela_de_nivel_diario()
            
             elif opcao10 == 2:
                 limpar_terminal()
                 Tela_menu()
    
    

def Tela_de_nivel_diario():
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
        print("(1) Levantamento de Dados")
        print("(2) Obter Dicas")
        print("(3) Menu Principal")
        print("(4) Sustentabilidade Mensal")
        print("(5) Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            limpar_terminal()
            Tela_de_levantamento_de_dados_diario()  
            
        elif opcao == "2":
            limpar_terminal()
            Tela_de_dicas()
    
        elif opcao == "3": 
            limpar_terminal()
            Tela_principal()
            
        elif opcao == "4": 
            limpar_terminal()
            Tela_sustentabilidade_mensal()
            
        elif opcao == "5":
            limpar_terminal()
            Tela_de_saida()
            
            break
        else:
            print("\nOpção inválida! Digite uma opção válida!")
            
            
def Tela_de_levantamento_de_dados_diario():
        from tela_principal import Tela_de_dicas
        from tela_menu import Tela_menu
        from tela_principal import Tela_de_saida
        
<<<<<<< Updated upstream
=======
        conexao = conectar()
        cursor = conexao.cursor()
    
        comando = "SELECT pontuacao FROM respostas_desafios WHERE id_usuario = %s"
    
        cursor.execute(comando, (usuario_logado["id"],))
        resultado = cursor.fetchall()
    
        cursor.close()
        conexao.close()

        
        #desafios_diarios = [sum(linha) for linha in resultado]
        
>>>>>>> Stashed changes
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
        print("LEVANTAMENTO DE DADOS")
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
            print("(1) Voltar a Tela de Nível")
            print("(2) Obter Dicas")
            print("(3) Menu Principal")
            print("(4) Sustentabilidade Mensal")
            print("(5) Sair")
            opcao9 = int(input("Digite a opção desejada: "))
        
            if opcao9 == 1:
                limpar_terminal()
                Tela_de_nivel_diario()
            
            elif opcao9==2:
                limpar_terminal()
                Tela_de_dicas()
            
            elif opcao9==3:
                limpar_terminal()
                Tela_menu()
            
            elif opcao9== 4:
                limpar_terminal()
                Tela_sustentabilidade_mensal()
        
            elif opcao9== 5:
                print("\nVocê encerrou o programa. Até mais!")
                limpar_terminal()
                Tela_de_saida()
            
            else:
                print("\nOpção inválida! Tente novamente.")

def Tela_sustentabilidade_mensal():
    from tela_menu import Tela_menu
    print("----------------------------------------------------------------------")
    print("SUSTENTABILIDADE MENSAL")
    print("----------------------------------------------------------------------")

    #Entrada de dados:

    desafiodia1=40
    desafiodia2=40
    desafiodia3=40
    desafiodia4=40
    desafiodia5=40
    desafiodia6=40
    desafiodia7=40
    desafiodia8=40
    desafiodia9=40
    desafiodia10=40
    desafiodia11=40
    desafiodia12=40
    desafiodia13=40
    desafiodia14=40
    desafiodia15=40
    desafiodia16=40
    desafiodia17=40
    desafiodia18=40
    desafiodia19=40
    desafiodia20=40
    desafiodia21=40
    desafiodia22=40
    desafiodia23=40
    desafiodia24=40
    desafiodia25=40
    desafiodia26=40
    desafiodia27=40
    desafiodia28=40
    desafiodia29=40
    desafiodia30=40


    #Calculo Sustentabilidade mensal:
    Smensal = (desafiodia1+desafiodia2+desafiodia3+desafiodia4+desafiodia5+desafiodia6+desafiodia7+desafiodia8+desafiodia9+desafiodia10+desafiodia11+desafiodia12+desafiodia13+desafiodia14+desafiodia15+desafiodia16+desafiodia17+desafiodia18+desafiodia19+desafiodia20+desafiodia21+desafiodia22+desafiodia23+desafiodia24+desafiodia25+desafiodia26+desafiodia27+desafiodia28+desafiodia29+desafiodia30)/30

    if (30 <= Smensal <= 40):
        print("PARABÉNS, SUA SUSTENTABILIDADE MENSAL É: ALTA!")
        
    elif (20 <= Smensal <=29):
        print("SEU NÍVEL DE SUSTENTABILIDADE MENSAL É: MODERADA!")
        
    else:
        print("SEU NÍVEL DE SUSTENTABILIDADE MENSAL É: BAIXA!")
        
    while True:
        print("")
        print("Digite para continuar: (1) Tela de Nível ou (2) Menu Principal")
        print("")
        opcao22= input("Digite a opção desejada: ")
        if opcao22=="1":
            limpar_terminal()
            Tela_de_nivel_diario()
        elif opcao22=="2":
            limpar_terminal()
            Tela_menu()
        else:
            print("Opção inválida. Digite uma opção válida!")




