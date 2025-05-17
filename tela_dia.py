import os
from colorama import Fore, Style
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def Tela_dia(usuario_logado, pontos1, pontos2, pontos3, pontos4):
    from tela_principal import Tela_de_dicas
    from tela_principal import Tela_principal
    from tela_principal import Tela_de_saida
    from tela_desafios import Tela_opcoes
     
    while True:
        print("----------------------------------------------------------------------")
        print(Fore.YELLOW+"\nPARABÉNS, VOCÊ CONCLUIU O DESAFIO SUSTENTAÍ!\n"+Style.RESET_ALL)
        print("Agora você poderá saber o quão sustentável você é!\n")
     
        variavel_do_nivel=(pontos1+pontos2+pontos3+pontos4)
        
        if (variavel_do_nivel>=30) and (variavel_do_nivel<=40):
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É: ", Fore.YELLOW+"ALTO!"+Style.RESET_ALL)
            print("----------------------------------------------------------------------")
            
        elif (variavel_do_nivel>=20) and (variavel_do_nivel<=29):
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É: ", Fore.YELLOW+"MÉDIO!"+Style.RESET_ALL)
            print("----------------------------------------------------------------------")
            
        else:
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É: ", Fore.YELLOW+"BAIXO!"+Style.RESET_ALL)
            print("----------------------------------------------------------------------")
            print("")
            print("Mas fique tranquilo(a), vamos te ajudar a melhorar...")
            
        print("\nEscolha uma opção:")
        print("1 - MENU OPÇÕES")
        print("2 - OBTER DICAS")
        print("3 - MENU PRINCIPAL")
        print("4 - FECHAR PROGRAMA")
        
        opcao = int(input("\nDigite a opção desejada: "))
        
        if opcao == 1:
            limpar_terminal()
            Tela_opcoes(usuario_logado)  
            
        elif opcao == 2:
            limpar_terminal()
            Tela_de_dicas(usuario_logado)
    
        elif opcao == 3: 
            limpar_terminal()
            Tela_principal()
            
        elif opcao == 4:
            limpar_terminal()
            Tela_de_saida(usuario_logado)
            
            break
        else:
            print("\nOpção inválida! Digite uma opção válida!")
