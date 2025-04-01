pontos1=10
pontos2=10
pontos3=10
pontos4=10



# comentário adicionado para testar o commit no github



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
    """Exibe a tela de boas-vindas e processa a entrada do usuÃ¡rio."""
    print(" ")
    print("BEM VINDO AO SUSTENTAÍ")
    print("")
    print("A sustentabilidade começa com pequenas escolhas diárias que fazem uma grande diferençaa no mundo. O Sustentaí­ é um projeto criado para inspirar e desafiar você a viver de forma mais sustentável.")
    
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
        exibir_como_funciona()
    elif opcao == "2":
        tela_login()
    elif opcao == "3":
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
    print("O Desafio se baseia em 4 fases (Consumo de água, energia, resí­duos e transporte). Para cada fase há uma classificação podendo ser (Alta, Moderada e Baixa Sustentabilidade), com uma determinada pontuação para cada (Alta = 10; Moderada = 5; Baixa = 2). Ao final do Desafio diário somaremos cada classificação de cada fase, obtendo uma pontuação que determinará seu ní­vel total de sustentabilidade. Observe abaixo a ponderação para seu ní­vel total de sustentabilidade:")
    print("")

    
    lista_sustentabilidade = criar_lista_sustentabilidade()
    exibir_lista_sustentabilidade(lista_sustentabilidade)

    input("\nPara voltar ao menu principal pressione Enter")
    tela_boas_vindas()




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
    tela_boas_vindas()
    


def tela_login():
    print("\n------------------------------------------------------------------")
    print("LOGIN")
    print("------------------------------------------------------------------")
    print("")
    print("OlÁ! Para começarmos nosso desafio, precisamos te conhecer!")

    while True:
        try:
            usuario = input("\nDigite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
        
            if(usuario == "admin" and senha == "admin"):
                tela_desafios()
                break
            else:
                print("\n Usuário ou senha errado")
        except ValueError as e:
                    print(e)
                    print("Tente Novamente")
   
def tela_desafios():
    print("")
    print("------------------------------------------------------------------")
    print("DESAFIOS")
    print("------------------------------------------------------------------")
    print("\n1. DESAFIO ÁGUA")
    print("2. DESAFIO RESÍDUOS")
    print("3. DESAFIO ENERGIA")
    print("4. DESAFIO TRANSPORTE")

    print("")
    print("Clique em 1 DESAFIO - ÁGUA para começar o desafio")
    

    desafio0 = int(input("\nDigite a opção escolhida:"))
    print("")


# Inicia o programa
tela_boas_vindas()

# desafios
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
consumoagua=float(input("Qual o seu consumo de água em metros cúbicos (m*3)?"))
print("")
print("----------------------------------------------------------------------")

#conta metros cubicos para litros:
consumoagua1=consumoagua*1000

if (consumoagua1<150):
    print("Seu nível no DESAFIO 1 - ÁGUA é: ALTA SUSTENTABILIDADE ")
if ((consumoagua1>=150) and (consumoagua1<=200)):
    print("Seu nível no DESAFIO 1 - ÁGUA é: MODERADA SUSTENTABILIDADE ")
if (consumoagua1>200):
    print("Seu nível no DESAFIO 1 - ÁGUA é: BAIXA SUSTENTABILIDADE ")


print("----------------------------------------------------------------------")
print("Escolha uma opção: 1- CONTINUAR")
print("")
opcao1=float(input("Digite a opção escolhida:"))
print("")

if (opcao1==1):
    print("----------------------------------------------------------------------")
    print("DESAFIOS")
    print("----------------------------------------------------------------------")
    print("")
    print("DESAFIO 1 - ÁGUA:            CONCLUIDO")
    print("DESAFIO 2 - RESÍDUOS:    NÃO CONCLUIDO")
    print("DESAFIO 3 - ENERGIA:     NÃO CONCLUIDO")
    print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
    print("")
    print("Clique em 2 DESAFIO - RESÍDUOS para continuar o desafio")
    print("")
    opcao2=float(input("Digite a opção escolhida:")) 
    
if (opcao2==2):
    print("")
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
    print("")
    consumoresiduos1=float(input("Quanto pesa seu lixo reciclável em gramas(g)? "))
    print("")
    print("Escolha uma opção: 1 - CONTINUAR")
    print("")
    opcao3=float(input("Digite a opção escolhida: "))
    print("")
    
if (opcao3==1):
    print("----------------------------------------------------------------------")
    print("")
    print("DESAFIO RESÍDUOS PARTE 2")
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
    print("")
    consumoresiduos2=float(input("Quanto pesa seu lixo não reciclável em gramas(g)? "))
    print("")
    print("----------------------------------------------------------------------") 

if (consumoresiduos1>consumoresiduos2*1.5):
    print("Seu nível no DESAFIO 2 - RESÍDUOS é: ALTA SUSTENTABILIDADE")
elif ((consumoresiduos1>=consumoresiduos2*1.2) and (consumoresiduos1<=consumoresiduos2*1.5)):
    print("Seu nível no DESAFIO 2 - RESÍDUOS é: MODERADA SUSTENTABILIDADE")
elif (consumoresiduos1<consumoresiduos2*0.8):
    print("Seu nível no DESAFIO 2 - RESÍDUOS é: BAIXA SUSTENTABILIDADE")
else:
    print("Seu nível no DESAFIO 2 - RESÍDUOS é: BAIXA SUSTENTABILIDADE")

print("----------------------------------------------------------------------")     
print("Escolha uma opção: 1- CONTINUAR")
print("")
opcao4=float(input("Digite a opção escolhida:"))
print("")   


if (opcao4==1):
    print("----------------------------------------------------------------------") 
    print("DESAFIOS")
    print("----------------------------------------------------------------------") 
    print("")
    print("DESAFIO 1 - ÁGUA:            CONCLUIDO")
    print("DESAFIO 2 - RESÍDUOS:        CONCLUIDO")
    print("DESAFIO 3 - ENERGIA:     NÃO CONCLUIDO")
    print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
    print("")
    print("Clique em 3 DESAFIO - ENERGIA para continuar o desafio")
    print("")
    

# -*- coding: utf-8 -*-

#Código parte - Lucas


desafio1 = int(input("Digite a opção escolhida: "))
print("")

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
    print("")

    kwh = float(input("Digite quanto você gasta de energia em Kwh: "))
    print("")
    print("----------------------------------------------------------------------") 

    # Nível de sustentabilidade para energia
    if kwh < 100:
        print("Seu nível no DESAFIO 3 - ENERGIA É: ALTA SUSTENTABILIDADE")
    elif 100 <= kwh <= 200:
        print("Seu nível no DESAFIO 3 - ENERGIA É: MODERADA SUSTENTABILIDADE")
    else:
        print("Seu nível no DESAFIO 3 - ENERGIA É: BAIXA SUSTENTABILIDADE")

# DESAFIO 4 - TRANSPORTE
print("----------------------------------------------------------------------") 
print("Escolha uma opção: 1- CONTINUAR")
print("")
opcao8=float(input("Digite a opção escolhida:"))
print("")   

if (opcao8==1):
    print("----------------------------------------------------------------------")
    print("DESAFIOS")
    print("----------------------------------------------------------------------")
    print("") 
    print("DESAFIO 1 - ÁGUA:            CONCLUIDO")
    print("DESAFIO 2 - RESÍDUOS:        CONCLUIDO")
    print("DESAFIO 3 - ENERGIA:         CONCLUIDO")
    print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
    print("")
    print("Clique em 4 DESAFIO - TRANSPORTE para continuar o desafio")
    print("")

    desafio2 = int(input("Digite a opção escolhida: "))
    print("")


if desafio2 == 4:
    print("----------------------------------------------------------------------")
    print("DESAFIO 4 - TRANSPORTE")
    print("----------------------------------------------------------------------")
    print("")
    print("\nExcelente! Você passou por quase todos os desafios, conclua o desafio 4 para descobrir o quão sustentável você é.")
    print("")
    print("Qual meio de transporte você utilizou hoje? (preencha com 0 para os que não utilizou)")
    print("")

    meiotransp1 = int(input("\nSem gasto de energia e com energia elétrica (a pé, bicicleta, patinete ou outro meio): "))
    meiotransp2 = int(input("\nComunitário (ônibus, carona ou outro meio): "))
    meiotransp3 = int(input("\nPrivado e combustíveis fósseis (carro): "))
    print("")
    print("----------------------------------------------------------------------")
    # Nível de sustentabilidade para transporte
    total_transporte = meiotransp1 + meiotransp2 + meiotransp3

    if meiotransp1 > meiotransp2 and meiotransp1 > meiotransp3:
        print("Seu nível no DESAFIO 4 - TRANSPORTE É: ALTA SUSTENTABILIDADE")
    elif meiotransp2 > meiotransp1 and meiotransp2 > meiotransp3:
        print("Seu nível no DESAFIO 4 - TRANSPORTE É: MODERADA SUSTENTABILIDADE")
    else:
        print("Seu nível no DESAFIO 4 - TRANSPORTE É: BAIXA SUSTENTABILIDADE")

print("----------------------------------------------------------------------")

def menu_principal():
    while True:
        print("\nPARABÉNS, VOCÊ CONLUIU O DESAFIO SUSTENTAÍ!")
        print("")
        print("Agora você podera saber o quão sustentável você é!")
        print("")
        variavel_do_nivel=(pontos1+pontos2+pontos3+pontos4)
        if (variavel_do_nivel>30) or (variavel_do_nivel<40):
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É ALTA!")
            print("----------------------------------------------------------------------")
        elif (variavel_do_nivel>20) or (variavel_do_nivel<29):
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É MODERADA!")
            print("----------------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É BAIXO!")
            print("----------------------------------------------------------------------")
            print("")
            print("Mas fique tranquilo(a), vamos te ajudar a melhorar...")
        print("\nAgora escolha uma opção: ")
        print("1. LEVANTAMENTOS DE DADOS")
        print("2. SAIR E ENCERRAR O PROGRAMA")
        print("")
        
        op=int(input("Digite a opção desejada: "))
        if (op==2):
            print("\nVocê encerrou o programa.")
        elif (op == 1):
            print("\nTela de levantamento de dados")
            tela_de_nivel()
        else:
            print("Opção inválida! Digite uma opção válida.")
            
menu_principal()
#SAIR
#LEVANTAMENTO DE DADOS
#DICAS

def tela_de_nivel():
    while True:
        print("\n----------------------------------------------------------------------\n")
        print("LEVANTAMENTO DE DADOS")
        print("Vamos ver detalhes da sua performance...")
        print("\nAgora você poderá saber o quão sustentável você é e onde pode melhorar, caso necessário!")
        print("Nível de sustentabilidade de acordo com cada desafio: ")
        print(f"\nDesafio 1: {pontos1} pontos")
        print(f"\nDesafio 2: {pontos2} pontos")
        print(f"\nDesafio 3: {pontos3} pontos")
        print(f"\nDesafio 4: {pontos4} pontos")
        total_pontos = pontos1 + pontos2 + pontos3 + pontos4 #Posso adicionar os pontos para cálculo final nas demais telas?
        if total_pontos > 0:
            porcentagem1 = (pontos1 / total_pontos) * 100
            porcentagem2 = (pontos2 / total_pontos) * 100
            porcentagem3 = (pontos3 / total_pontos) * 100
            porcentagem4 = (pontos4 / total_pontos) * 100
        print("\nDistribuição percentual dos pontos:")
        print(f"\nDesafio 1: {porcentagem1:.2f}%")
        print(f"\nDesafio 2: {porcentagem2:.2f}%")
        print(f"\nDesafio 3: {porcentagem3:.2f}%")
        print(f"\nDesafio 4: {porcentagem4:.2f}%")
        
while True:
    print("\nEscolha uma opção:")
    print("(1) Voltar ao menu principal")
    print("(2) Obter dicas")
    print("(3) Sair")
    opcao9 = int(input("Digite a opção desejada: "))
    if opcao9 == 1:
        print("\nVoltando ao menu principal...")
    elif opcao9==2:
        print("Tela de dicas") #Como voltar?
    elif opcao9== 3:
        print("\nVocê encerrou o programa. Até mais!")
    else:
        print("\nOpção inválida! Tente novamente.")
        
tela_de_nivel()

