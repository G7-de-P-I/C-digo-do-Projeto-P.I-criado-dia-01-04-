# -*- coding: utf-8 -*-

#Código parte - Lucas

print("\nDESAFIOS")
print("\n-------------------------------------")
print("\n1. Desafio água (concluído)")
print("2. Desafio resíduos (concluído)")
print("3. Desafio energia")
print("4. Desafio transporte")
print("\n-------------------------------------")

desafio1 = int(input("\nEscolha um desafio que ainda não foi concluído, para fazê-lo. Digite 3 para energia ou 4 para transporte: "))

# DESAFIO 3 - ENERGIA
if desafio1 == 3:
    print("\nDESAFIO 3 - ENERGIA")
    print("\n--------------------------------------")
    print("\nQuase lá! Estamos perto de saber seu nível de sustentabilidade! Saber seu consumo de energia é essencial para completar o desafio.")
    print("\n--------------------------------------")
    print("\nComo verificar seu consumo:")
    print("\n1. Pegue sua conta de energia -")
    print("Encontre a fatura referente ao mês atual.")
    print("\n2. Localize o consumo mensal -")
    print("Procure a informação de consumo total, geralmente expressa em kWh (quilowatt-hora).")
    print("\n--------------------------------------")

    kwh = float(input("\nDigite quanto você gasta de energia em Kwh: "))

    # Nível de sustentabilidade para energia
    if kwh < 100:
        print("Seu nível no DESAFIO 3 - ENERGIA É: ALTA SUSTENTABILIDADE")
    elif 100 <= kwh <= 200:
        print("Seu nível no DESAFIO 3 - ENERGIA É: MODERADA SUSTENTABILIDADE")
    else:
        print("Seu nível no DESAFIO 3 - ENERGIA É: BAIXA SUSTENTABILIDADE")

# DESAFIO 4 - TRANSPORTE
print("\nDESAFIOS")
print("\n-------------------------------------")
print("\n1. Desafio água (concluído)")
print("2. Desafio resíduos (concluído)")
print("3. Desafio energia (concluído)")
print("4. Desafio transporte")
print("\n-------------------------------------")

desafio2 = int(input("\nEscolha um desafio que ainda não foi concluído, para fazê-lo. Digite 4 para transporte: "))

if desafio2 == 4:
    print("\nDESAFIO 4 - TRANSPORTE")
    print("\n----------------------------------------")
    print("\nExcelente! Você passou por quase todos os desafios, conclua o desafio 4 para descobrir o quão sustentável você é.")
    print("\n----------------------------------------")
    print("\nQual meio de transporte você utilizou hoje? (preencha com 0 para os que não utilizou)")
    print("\n----------------------------------------")

    meiotransp1 = int(input("\nSem gasto de energia e com energia elétrica (a pé, bicicleta, patinete ou outro meio): "))
    meiotransp2 = int(input("\nComunitário (ônibus, carona ou outro meio): "))
    meiotransp3 = int(input("\nPrivado e combustíveis fósseis (carro): "))

    # Nível de sustentabilidade para transporte
    total_transporte = meiotransp1 + meiotransp2 + meiotransp3

    if meiotransp1 > meiotransp2 and meiotransp1 > meiotransp3:
        print("Seu nível no DESAFIO 4 - TRANSPORTE É: ALTA SUSTENTABILIDADE")
    elif meiotransp2 > meiotransp1 and meiotransp2 > meiotransp3:
        print("Seu nível no DESAFIO 4 - TRANSPORTE É: MODERADA SUSTENTABILIDADE")
    else:
        print("Seu nível no DESAFIO 4 - TRANSPORTE É: BAIXA SUSTENTABILIDADE")

print("\n-------------------------------------")