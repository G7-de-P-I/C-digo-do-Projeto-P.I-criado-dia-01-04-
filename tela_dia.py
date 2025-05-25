# Importa o módulo 'os' para executar comandos do sistema operacional, como limpar o terminal
import os

# Importa do pacote 'colorama' as classes Fore e Style para manipular cores e estilos no texto do terminal
from colorama import Fore, Style

# Função que limpa a tela do terminal
def limpar_terminal():
    # Executa o comando 'cls' no Windows e 'clear' em sistemas Unix/Linux/Mac para limpar a tela
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que exibe a tela de resultado do dia, mostrando o nível de sustentabilidade com base nos pontos recebidos
def Tela_dia(usuario_logado, pontos1, pontos2, pontos3, pontos4):
    # Importa a função Tela_de_dicas da tela_principal para mostrar dicas ao usuário
    from tela_principal import Tela_de_dicas
    # Importa a função Tela_principal da tela_principal para voltar ao menu principal
    from tela_principal import Tela_principal
    # Importa a função Tela_de_saida da tela_principal para finalizar ou sair do programa
    from tela_principal import Tela_de_saida
    # Importa a função Tela_opcoes da tela_desafios para mostrar o menu de opções de desafios
    from tela_desafios import Tela_opcoes
     
    # Loop que mantém o menu ativo até o usuário escolher sair
    while True:
        print("----------------------------------------------------------------------")
        # Mensagem de parabéns com texto em amarelo usando colorama
        print(Fore.YELLOW + "\nPARABÉNS, VOCÊ CONCLUIU O DESAFIO SUSTENTAÍ!\n" + Style.RESET_ALL)
        print("Agora você poderá saber o quão sustentável você é!\n")
     
        # Soma os pontos dos quatro desafios para calcular o nível
        variavel_do_nivel = (pontos1 + pontos2 + pontos3 + pontos4)
        
        # Condicional para determinar o nível de sustentabilidade baseado na soma dos pontos
        if (variavel_do_nivel >= 30) and (variavel_do_nivel <= 40):
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É: ", Fore.YELLOW + "ALTO!" + Style.RESET_ALL)
            print("----------------------------------------------------------------------")
            
        elif (variavel_do_nivel >= 20) and (variavel_do_nivel <= 29):
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É: ", Fore.YELLOW + "MÉDIO!" + Style.RESET_ALL)
            print("----------------------------------------------------------------------")
            
        else:
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É: ", Fore.YELLOW + "BAIXO!" + Style.RESET_ALL)
            print("----------------------------------------------------------------------")
            print("")
            # Mensagem motivacional para incentivar o usuário a melhorar
            print("Mas fique tranquilo(a), vamos te ajudar a melhorar...")
            
        # Exibe as opções para o usuário navegar pelo programa
        print("\nEscolha uma opção:")
        print("1 - MENU OPÇÕES")
        print("2 - OBTER DICAS")
        print("3 - MENU PRINCIPAL")
        print("4 - FECHAR PROGRAMA")
        
        # Recebe a opção escolhida pelo usuário e converte para inteiro
        opcao = int(input("\nDigite a opção desejada: "))
        
        # Verifica a opção e chama a função correspondente
        if opcao == 1:
            limpar_terminal()             # Limpa o terminal para melhor visualização
            Tela_opcoes(usuario_logado)  # Exibe o menu de opções de desafios
            
        elif opcao == 2:
            limpar_terminal()             
            Tela_de_dicas(usuario_logado) # Mostra dicas para o usuário
            
        elif opcao == 3: 
            limpar_terminal()             
            Tela_principal()             # Volta para a tela principal do programa
            
        elif opcao == 4:
            limpar_terminal()             
            Tela_de_saida(usuario_logado) # Finaliza a sessão ou fecha o programa
            
            break  # Sai do loop e encerra a função
            
        else:
            # Caso o usuário digite uma opção inválida, mostra essa mensagem de erro
            print("\nOpção inválida! Digite uma opção válida!")