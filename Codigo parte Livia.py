#DESAFIO SUSTENTAÍ
#CODIGO - PARTE LIVIA
#SOFTWARE PARA DESAFIO SUSTENTAÍ
print("----------------------------------------------------------------------")
print("")
print("DESAFIO 1 - ÁGUA:")
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

#conta metros cubicos para litros:
consumoagua1=consumoagua*1000

if (consumoagua1<150):
    print("Seu nível no DESAFIO 1 - ÁGUA é: ALTA SUSTENTABILIDADE ")
if ((consumoagua1>=150) and (consumoagua1<=200)):
    print("Seu nível no DESAFIO 1 - ÁGUA é: MODERADA SUSTENTABILIDADE ")
if (consumoagua1>200):
    print("Seu nível no DESAFIO 1 - ÁGUA é: BAIXA SUSTENTABILIDADE ")

print("")
print("Escolha uma opção: 1- CONTINUAR 2- VOLTAR")
print("")
opcao=float(input("Digite a opção escolhida:"))
print("")

if (opcao==1):
    print("----------------------------------------------------------------------")
    print("TELA DE DESAFIOS")
    print("")
    print("DESAFIO 1 - ÁGUA:            CONCLUIDO")
    print("DESAFIO 2 - RESÍDUOS:    NÃO CONCLUIDO")
    print("DESAFIO 3 - ENERGIA:     NÃO CONCLUIDO")
    print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
    print("")
    print("Clique em (DESAFIO 2 - RESÍDUOS) para continuar o desafio")
    print("")
    print("Escolha uma opção: 1 - (DESAFIO 2 - RESÍDUOS)  2- VOLTAR")
    print("")
    opcao1=float(input("Digite a opção escolhida:"))
    
if (opcao1==1):
    print("")
    print("----------------------------------------------------------------------")
    print("DESAFIO 2 - RESÍDUOS:")
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
    print("Escolha uma opção: 1 - CONTINUAR 2- VOLTAR")
    print("")
    opcao3=float(input("Digite a opção escolhida: "))
    print("")
    
if (opcao1==2):
    print("----------------------------------------------------------------------")
    print("TELA INICIAL")

if (opcao==2):
    print("----------------------------------------------------------------------")
    print("TELA DE DESAFIOS")
    print("")
    print("DESAFIO 1 - ÁGUA:        NÃO CONCLUIDO")
    print("DESAFIO 2 - RESÍDUOS:    NÃO CONCLUIDO")
    print("DESAFIO 3 - ENERGIA:     NÃO CONCLUIDO")
    print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
    print("")
    print("Desafios não concluídos, clique em (DESAFIO 1 - ÁGUA) para começar")
    print("")
    print("Escolha uma opção: 1 - DESAFIO ÁGUA 2- VOLTAR")
    print("")
    opcao2=float(input("Digite a opção escolhida:"))
    
    
if (opcao2==1):
    print("----------------------------------------------------------------------")
    print("DESAFIO 1 - ÁGUA:")
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
   
#conta metros cubicos para litros:
consumoagua1=consumoagua*1000

if (consumoagua1<150):
    print("Seu nível no DESAFIO 1 - ÁGUA é: ALTA SUSTENTABILIDADE ")
if ((consumoagua1>=150) and (consumoagua1<=200)):
    print("Seu nível no DESAFIO 1 - ÁGUA é: MODERADA SUSTENTABILIDADE ")
if (consumoagua1>200):
    print("Seu nível no DESAFIO 1 - ÁGUA é: BAIXA SUSTENTABILIDADE ")

print("")
print("Escolha uma opção: 1- CONTINUAR 2- VOLTAR")
print("")
opcao=float(input("Digite a opção escolhida:"))
print("")


#JUNTAR COM TELA INICIAL
if (opcao2==2):
    print("----------------------------------------------------------------------")
    print("TELA INICIAL")
    
if (opcao1==1):
    print("")
    print("----------------------------------------------------------------------")
    print("DESAFIO 2 - RESÍDUOS:")
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
    print("Escolha uma opção: 1 - CONTINUAR 2- VOLTAR")
    print("")
    opcao3=float(input("Digite a opção escolhida: "))
    print("")
    
if (opcao1==2):
    print("----------------------------------------------------------------------")
    print("TELA INICIAL")
    

if (opcao3==1):
    print("----------------------------------------------------------------------")
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

if (consumoresiduos1>consumoresiduos2*1.5):
    print("Seu nível no DESAFIO 2 - RESÍDUOS é: ALTA SUSTENTABILIDADE")
if ((consumoresiduos1>=consumoresiduos2*1.2) and (consumoresiduos1<=consumoresiduos2*1.5)):
    print("Seu nível no DESAFIO 2 - RESÍDUOS é: MODERADA SUSTENTABILIDADE")
if (consumoresiduos1<consumoresiduos2*0.8):
    print("Seu nível no DESAFIO 2 - RESÍDUOS é: BAIXA SUSTENTABILIDADE")
    print("")
    print("Escolha uma opção: 1- CONTINUAR 2- VOLTAR")
    print("")
    opcao4=float(input("Digite a opção escolhida:"))
    print("")
    
if (opcao3==2):
    print("----------------------------------------------------------------------")
    print("TELA DE DESAFIOS")
    print("")
    print("DESAFIO 1 - ÁGUA:            CONCLUIDO")
    print("DESAFIO 2 - RESÍDUOS:    NÃO CONCLUIDO")
    print("DESAFIO 3 - ENERGIA:     NÃO CONCLUIDO")
    print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
    print("")
    print("Clique em (DESAFIO 2 - RESÍDUOS) para continuar o desafio")
    print("")
    print("Escolha uma opção: 1 - (DESAFIO 2 - RESÍDUOS)  2- VOLTAR")
    print("")
    opcao5=float(input("Digite a opção escolhida:"))

if (opcao4==1):
    print("TELA DE DESAFIOS")
    print("")
    print("DESAFIO 1 - ÁGUA:            CONCLUIDO")
    print("DESAFIO 2 - RESÍDUOS:        CONCLUIDO")
    print("DESAFIO 3 - ENERGIA:     NÃO CONCLUIDO")
    print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
    print("")
    print("CLIQUE NO (DESAFIO 3 - ENERGIA) PARA CONTINUAR O DESAFIO")
    print("")
    print("Escolha uma opção: 1 - (DESAFIO 3 - ENERGIA)  2- VOLTAR")
    print("")
    opcao6=float(input("Digite a opção escolhida:"))
    print("")
    
if (opcao6==1):
    print("----------------------------------------------------------------------")
    print("DESAFIO 3 - ENERGIA ")
if (opcao6==2):
    print("----------------------------------------------------------------------")
    print("TELA INICIAL:")
    
if (opcao4==2):
    print("----------------------------------------------------------------------")
    print("TELA DE DESAFIOS")
    print("")
    print("DESAFIO 1 - ÁGUA:            CONCLUIDO")
    print("DESAFIO 2 - RESÍDUOS:    NÃO CONCLUIDO")
    print("DESAFIO 3 - ENERGIA:     NÃO CONCLUIDO")
    print("DESAFIO 4 - TRANSPORTE:  NÃO CONCLUIDO")
    print("")
    print("Clique em (DESAFIO 2 - RESÍDUOS) para continuar o desafio")
    print("")
    print("Escolha uma opção: 1 - (DESAFIO 2 - RESÍDUOS)  2- VOLTAR")
    print("")
    opcao7=float(input("Digite a opção escolhida:"))
   
