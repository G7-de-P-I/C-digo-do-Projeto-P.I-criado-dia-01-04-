# -*- coding: utf-8 -*-

#Código parte - Lucas

def tela_desafio_ener_transp():
     while True:
         try:
             print("")
             desafio1 = int(input("Digite a opção escolhida: "))
             break
         except ValueError:
             print("")
             print("Erro: Digite uma opção numérica válida.")
     
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
             print("Seu nível no DESAFIO 3 - ENERGIA É: ALTA SUSTENTABILIDADE")
             
         elif 5 <= kwh <= 10:
             print("Seu nível no DESAFIO 3 - ENERGIA É: MODERADA SUSTENTABILIDADE")
             
         else:
             print("Seu nível no DESAFIO 3 - ENERGIA É: BAIXA SUSTENTABILIDADE")
     
     # DESAFIO 4 - TRANSPORTE
     
     print("----------------------------------------------------------------------") 
     print("")
     print("Escolha uma opção: 1 - CONTINUAR")
         
     while True:
         try:
             print("")
             opcao8 = int(input("Digite a opção escolhida: "))
             break
         except ValueError:
             print("")
             print("Erro: Digite uma opção válida.")
     
     print("")
     if opcao8 == 1:
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
         
         while True:
             try:
                 print("")
                 desafio2 = int(input("Digite a opção escolhida: "))
                 break
             except ValueError:
                 print("")
                 print("Erro: Digite uma opção numérica válida.")
     
         print("")
         
         if desafio2 == 4:
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
                 print("Seu nível no DESAFIO 4 - TRANSPORTE É: ALTA SUSTENTABILIDADE")
             elif meiotransp2 > meiotransp1 and meiotransp2 > meiotransp3:
                 print("Seu nível no DESAFIO 4 - TRANSPORTE É: MODERADA SUSTENTABILIDADE")
             else:
                 print("Seu nível no DESAFIO 4 - TRANSPORTE É: BAIXA SUSTENTABILIDADE")
     
     print("--------------------------------------------------------------------")
     
     # término parte - Lucas