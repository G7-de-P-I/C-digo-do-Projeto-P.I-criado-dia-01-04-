#PARTE - VICTÓRIA
    
#tela de saída e dicas
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
    exit()
            
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
    print("  Dica 5: REveja seu consumo de água, verificando se não há vazamentos em")
    print("sua casa/apartamento")
    print(" ")
    
    
    while True: 
        print(" Digite para continuar: (1) Tela de Nível ou (2) Menu Principal")
        opcao20= input("Digite a opção desejada: ")
        if opcao20=="1":
            tela_de_nivel_diario()
        elif opcao20=="2":
            tela_de_boas_vindas()
        else:
            print("Opção inválida. Digite uma opção válida!")
    
    

    
#COMEÇAR DAQUI
def tela_de_nivel_diario():
    while True:
        print("----------------------------------------------------------------------")
        print("\nPARABÉNS, VOCÊ CONLUIU O DESAFIO SUSTENTAÍ!\n")
        print("\nAgora você podera saber o quão sustentável você é!\n")
     
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
        print("(4) Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            tela_de_levantamento_de_dados_diario()  
        elif opcao == "2":
            tela_de_dicas()
        elif opcao == "3": 
            tela_de_boas_vindas()
        elif opcao == "4":
            tela_de_saida()
            break
        else:
            print("\nOpção inválida! Digite uma opção válida!")

#diária
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
        print("(4) Sair")
        opcao9 = int(input("Digite a opção desejada: "))
        
        if opcao9 == 1:
            tela_de_nivel_diario()
        elif opcao9==2:
            tela_de_dicas()
        elif opcao9==3:
            tela_de_boas_vindas()
        elif opcao9== 4:
            print("\nVocê encerrou o programa. Até mais!")
            tela_de_saida()
        else:
            print("\nOpção inválida! Tente novamente.")
tela_de_nivel_diario()

