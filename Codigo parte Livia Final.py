# -*- coding: utf-8 -*-

pontos1=10
pontos2=10
pontos3=10
pontos4=10

from rich.console import Console
from rich.table import Table
from datetime import datetime

console = Console()


def criar_lista_sustentabilidade():
    """Cria uma lista dos ní­veis de sustentabilidade."""

    sustentabilidade = [
        "Alta: 30 - 40  (10pts)",
        "Moderada: 20 - 29 (5pts)",
        "Baixa: 8 - 19  (2pts)"
    ]
    return sustentabilidade



def exibir_lista_sustentabilidade(lista):
    """Exibe a lista de sustentabilidade."""
    print("Ní­veis de Sustentabilidade:")
    for item in lista:
        print(f"- {item}")
        
        

def tela_boas_vindas():
    """Exibe a tela de boas-vindas e processa a entrada do usuário."""
    print(" ")
    print("BEM VINDO AO SUSTENTAÍ")
    print("")
    print("A sustentabilidade começa com pequenas escolhas diárias que fazem uma grande diferença no mundo. O Sustentaí­ é um projeto criado para inspirar e desafiar você a viver de forma mais sustentável.")
    
    print("")
    print("------------------------------------------------------------------")
    print("DESAFIO SUSTENTAÍ­")
    print("------------------------------------------------------------------")
    print("")
    print("Descubra seu ní­vel de sustentabilidade! Participe do nosso desafio e descubra como suas ações impactam o planeta. A cada passo, você aprende, evolui e contribui para um futuro mais verde e consciente. Está pronto para fazer a diferença? Vamos juntos nessa jornada sustentável!")
    print("\n1. COMO FUNCIONA")
    print("2. COMEÇAR")
    print("3. CADASTRAR")

    opcao = input("\nDigite uma opção (1 - 2 ou 3): ")

    if opcao == "1":
        console.clear()
        exibir_como_funciona()
    elif opcao == "2":
        console.clear()
        tela_login()
    elif opcao == "3":
        console.clear()
        tela_cadastro()
    else:
        print("Opção inválida. Tente novamente.")
        tela_boas_vindas()  # Chama a funÃ§Ã£o novamente para repetir o processo



def exibir_como_funciona():
    """Exibe o texto explicando como o Sustentaí­ funciona."""
    
    print("")
    print("------------------------------------------------------------------")
    print("COMO FUNCIONA:")
    print("------------------------------------------------------------------")
    print("")
    print("O Desafio se baseia em 4 fases (Consumo de água, energia, resí­duos e transporte). Para cada fase há uma classificação podendo ser (Alta, Moderada e Baixa Sustentabilidade), com uma determinada pontuação para cada (Alta = 10; Moderada = 5; Baixa = 2). Ao final do Desafio diário somaremos cada classificação de cada fase, obtendo uma pontuação que determinará seu ní­vel total de sustentabilidade diário e ao final de cada mês você receberá seu nível de sustentabilidade mensal. Observe abaixo a ponderação para seu ní­vel total de sustentabilidade:")
    print("")

    
    lista_sustentabilidade = criar_lista_sustentabilidade()
    exibir_lista_sustentabilidade(lista_sustentabilidade)

    input("\nPara voltar ao menu principal pressione Enter")
    console.clear()
    tela_boas_vindas()



def tela_desafios01():
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
        console.clear()
        tela_agua_residuos()
    
    elif opcao2 == 2:
        console.clear()
        tela_menu()
            
        
            
def tela_agua_residuos():
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
    
    #conta metros cubicos para litros:
    consumoagua1=consumoagua*1000
    
    if (consumoagua1<150):
        água = "ALTA SUSTENTABILIDADE"
        pontos1 = 10
        print("Seu nível no DESAFIO 1 - ÁGUA é: ALTA SUSTENTABILIDADE ")
        
    elif ((consumoagua1>=150) and (consumoagua1<=200)):
        água = "MODERADA SUSTENTABILIDADE"
        pontos1 = 5
        print("Seu nível no DESAFIO 1 - ÁGUA é: MODERADA SUSTENTABILIDADE ")
        
    else:
        água = "BAIXA SUSTENTABILIDADE"
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
        console.clear()
        tela_menu()
    
    elif (opcao1==1):
        console.clear()
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
        console.clear()
        tela_menu()
        
    elif (opcao2==1):
        console.clear()
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
        console.clear()
        tela_menu()
        
        
    elif (opcao3==1):
        console.clear()
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
        console.clear()
        tela_menu()
    
    elif (opcao4==1):
        console.clear()
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
                opcao5=float(input("Digite a opção escolhida: ")) 
                break
            except ValueError:
                print("")
                print("Erro: Digite um valor númerico válido para opção.")
                
        if opcao5 == 1:
            console.clear()
            tela_desafio_ener_transp()
        
        elif opcao5 == 2:
            console.clear()
            tela_menu
        

#Código parte - Lucas

def tela_desafio_ener_transp():
     
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
         console.clear()
         tela_menu()
         
     if opcao8 == 1:
         console.clear()
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
         
         if desafio2 == 2:
             console.clear()
             tela_menu()
         
         if desafio2 == 1:
             console.clear()
             print("----------------------------------------------------------------------")
             print("DESAFIO 4 - TRANSPORTE")
             print("----------------------------------------------------------------------")
             print("")
             print("Excelente! Você passou por quase todos os desafios, conclua o desafio 4 para descobrir o quão sustentável você é.")
             print("")
             print("Qual meio de transporte você utilizou hoje?")
             print("")
             print("Legenda:")
             print("")
             print("1 - Preencha com 1 se utilizou uma vez, com 2 se utilizou duas vezes e assim por diante")
             print("2 - Preencha com 0 se não utilizou nenhuma vez o meio de transporte")
             
             while True:
                 try:
                     meiotransp1 = int(input("\nSem gasto de energia elétrica (a pé, bicicleta, patinete ou outro meio): "))
                     break
                 except ValueError:
                     print("")
                     print("Erro: Digite um número válido.")
             
             while True:
                 try:
                     meiotransp2 = int(input("\nComunitário (ônibus, carona ou outro meio): "))
                     break
                 except ValueError:
                     print("")
                     print("Erro: Digite um número válido.")
             
             while True:
                 try:
                     meiotransp3 = int(input("\nPrivado e combustíveis fósseis (carro): "))
                     break
                 except ValueError:
                     print("")
                     print("Erro: Digite um número válido.")
             
             print("")
             print("----------------------------------------------------------------------")
     
             # Nível de sustentabilidade para transporte
             if meiotransp1 > meiotransp2 and meiotransp1 > meiotransp3:
                 transporte = "ALTA SUSTENTABILIDADE"
                 pontos4 = 10
                 print("Seu nível no DESAFIO 4 - TRANSPORTE É: ALTA SUSTENTABILIDADE")
                 
             elif meiotransp2 > meiotransp1 and meiotransp2 > meiotransp3:
                 transporte = "MODERADA SUSTENTABILIDADE"
                 pontos4 = 5
                 print("Seu nível no DESAFIO 4 - TRANSPORTE É: MODERADA SUSTENTABILIDADE")
                 
             else:
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
         console.clear()
         tela_de_nivel_diario()
    
     elif opcao10 == 2:
         console.clear()
         tela_menu()
     
     
     # término parte - Lucas

def tela_de_nivel_diario():
    while True:
        print("----------------------------------------------------------------------")
        print("\nPARABÉNS, VOCÊ CONLUIU O DESAFIO SUSTENTAÍ!\n")
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
            console.clear()
            tela_de_levantamento_de_dados_diario()  
            
        elif opcao == "2":
            console.clear()
            tela_de_dicas()
    
        elif opcao == "3": 
            console.clear()
            tela_boas_vindas()
            
        elif opcao == "4": 
            console.clear()
            tela_sustentabilidade_mensal()
            
        elif opcao == "5":
            console.clear()
            tela_de_saida()
            
            break
        else:
            print("\nOpção inválida! Digite uma opção válida!")
            
def tela_de_levantamento_de_dados_diario():
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
    print(" ")
    print("----------------------------------------------------------------------")
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
            console.clear()
            tela_de_nivel_diario()
            
        elif opcao9==2:
            console.clear()
            tela_de_dicas()
            
        elif opcao9==3:
            console.clear()
            tela_menu()
            
        elif opcao9== 4:
            console.clear()
            tela_sustentabilidade_mensal()
        
        elif opcao9== 5:
            print("\nVocê encerrou o programa. Até mais!")
            console.clear()
            tela_de_saida()
            
        else:
            print("\nOpção inválida! Tente novamente.")

def tela_sustentabilidade_mensal():
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
            
def tela_de_dicas():
    print("------------------------------------------------------------------------------")
    print("\nTELA DE DICAS\n")
    print("------------------------------------------------------------------------------")
    print("\n  Dica 1: Reduza o consumo de plástico, principalmente em embalagens")
    print("de produtos frequentes na sua rotina, como: alimentos, bebidas e cosméticos")
    print("  Dica 2: Economize energia elétrica apagando as luzes em comodos não utilizados")
    print("utilizados no momento e desligando eletrodomésticos de uso simplório")
    print("  Dica 3: Separe seu lixo para reciclagem")
    print("  Dica 4: Faça o uso de mais transportes públicos e evite pegar Táxi/Uber")
    print("em curtas distâncias")
    print("  Dica 5: Reveja seu consumo de água, verificando se não há vazamentos em")
    print("sua casa/apartamento")
    print(" ")
    
    
    while True: 
        print(" Digite para continuar: (1) Tela de Nível ou (2) Menu Principal")
        opcao20= input("Digite a opção desejada: ")
        if opcao20=="1":
            console.clear()
            tela_de_nivel_diario()
        elif opcao20=="2":
            console.clear()
            tela_menu()
        else:
            print("Opção inválida. Digite uma opção válida!")
            
#tela de saída e dicas

import sys

def tela_de_saida():
    print("-------------------------------------------------------------------------------")
    print("\n TELA DE SAÍDA\n")
    print("-------------------------------------------------------------------------------")
    print("\n Parabéns por ter terminado nosso programa!")
    print("Esperamos que tenha gostado :)")
    print(" Até a próxima!")
    print(" ")
    print(" ")
    print("\n**Esse progranma foi idealizado e construído pelos alunos de")
    print("engenharia de software, Grupo G7, da turma 103. Puc-Campinas.**")
    print(" ")
    print(" ")
    print("******************************************************************************")
    sys.exit()
            

def tela_cadastro():
    print("")
    print("------------------------------------------------------------------")
    print("CADASTRO")
    print("------------------------------------------------------------------")
    
    nome = input("\n Nome: ")
    email = input("\n Email: ")
    cpf = int(input("\n CPF: "))
    cep = int(input("\n CEP: "))
    senha = input("\n Senha: ")
    print("\n\n Cadastro Realizado!!")
    input("\nPara continuar pressione Enter")
    console.clear()
    tela_boas_vindas()
    
    
    
    
def tela_perfil():
    print("------------------------------------------------------------------")
    print("PERFIL")
    print("------------------------------------------------------------------")
    
    print("\nOlá [fulano], aqui estão alguns informações que podem ser úteis para você!!")
    print("\nNível sustentável de hoje: ...")
    print("\nNome: ...")
    print("Email: ...")
    print("Telefon: ...")
    print("CPF: ...")
    input("\nPara VOLTAR pressione Enter")
    console.clear()
    tela_menu()
    
    
    
    
def tela_historico():
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
            console.clear()
            tela_menu()
        try:
            data_formatada = datetime.strptime(data_input, "%d/%m/%Y").strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Formato inválido! Use DD/MM/AAAA.")
            
    console.clear()
    
    print("MUDANDO INFORMAÇÕES DOS DESAFIOS - DIA { data chamada }")
    tela_desafios01()
    
    
def tela_menu():
        print("------------------------------------------------------------------")
        print("MENU")
        print("------------------------------------------------------------------")
        print("\n1. DESAFIOS")  
        print("2. PERFIL")
        print("3. HÍSTORICO SUSTENTÁVEL")
        
        while True:
            try:
                Telair = int(input("\nDigite o número para ser direcionado para tela: "))
               
                if (Telair == 1):
                    console.clear()
                    tela_desafios01()
                if( Telair == 2):
                    console.clear()
                    tela_perfil()
                elif( Telair == 3):
                    console.clear()
                    tela_historico()
                else:
                    print("\n !!Opção inválida! Digite os números correpondentes!! ")  
               
            except ValueError:
                print("\n------------------------------------------------------------------")
                print("\nTente Novamente")

def tela_login():
    print("----------------------------------------------------------------")
    print("LOGIN")
    print("----------------------------------------------------------------")
    print("")
    print("Olá! Para começarmos nosso desafio, precisamos te conhecer!")

    while True:
        try:
            print("")
            resposta = input("Possui cadastro?(SIM/NÃO): ")
            
            if(resposta == "SIM" or resposta == "sim" or resposta == "Sim"):
                usuario = input("\nDigite seu nome de usuário: ")
                senha = input("Digite sua senha: ")
        
                if(usuario == "admin" and senha == "admin"):
                    console.clear()
                    tela_menu()
                else:
                    print("\n Usuário ou senha errado")
            else:
                console.clear()
                print("\n----------------------------------------------------------------")
                print("REALIZE SEU CADASTRO PRIMEIRO")
                tela_cadastro()
        except ValueError as e:
                    print(e)
                    print("Tente Novamente")
tela_boas_vindas()