import os
from banco import conectar

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

pontos1=10
pontos2=10
pontos3=10
pontos4=10

def Tela_desafio():
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
     cursor = None
     conexao = None

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

         try:
             conexao = conectar()
             cursor = conexao.cursor()

             comando = "INSERT INTO tabela_desafios (desa_enrgia) values (%s)"
             valor = (kwh)

             cursor.execute(comando,valor)
             conexao.commit()

             print("\n✅ Inserção de informação realizado com sucesso!")
         except Exception as e:
             print(f"\n❌ Erro ao inserir valor no banco de dados: {e}")
         finally:
             if cursor:
                 cursor.close()
             if conexao:
                 conexao.close()
     
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
        print("Seu nível no DESAFIO 1 - ÁGUA é: ALTA SUSTENTABILIDADE ")
        
    elif ((consumoagua1>=150) and (consumoagua1<=200)):
        agua = "MODERADA SUSTENTABILIDADE"
        pontos1 = 5
        print("Seu nível no DESAFIO 1 - ÁGUA é: MODERADA SUSTENTABILIDADE ")
        
    else:
        agua = "BAIXA SUSTENTABILIDADE"
        pontos1 = 2
        print("Seu nível no DESAFIO 1 - ÁGUA é: BAIXA SUSTENTABILIDADE ")
    
    
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
        
        
    elif (opcao3==1):
        limpar_terminal()
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




