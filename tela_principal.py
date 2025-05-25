import mysql.connector  # Para conexão com banco de dados (ainda não usado neste trecho)
import sys  # Para encerramento do programa com sys.exit()
from rich.console import Console  # Biblioteca para saída formatada no terminal
from rich.table import Table  # Para tabelas no terminal (não utilizado aqui, mas importado)
from datetime import datetime  # Para manipulação de datas (ainda não usado aqui)
from tela_desafios import Tela_opcoes  # Função importada de outro módulo
import os  # Para comandos de sistema como limpar o terminal
from colorama import Fore, Style

# Função para limpar o terminal, dependendo do sistema operacional
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Pontuação padrão atribuída para as 4 fases do desafio
pontos1 = 10
pontos2 = 10
pontos3 = 10
pontos4 = 10


# Cria uma lista com os níveis de sustentabilidade e sua pontuação correspondente
def criar_lista_sustentabilidade():
    sustentabilidade = [
        "Alta: 30 - 40  (10pts)",
        "Moderada: 20 - 29 (5pts)",
        "Baixa: 8 - 19  (2pts)"
    ]
    return sustentabilidade


# Exibe a lista de sustentabilidade no terminal
def exibir_lista_sustentabilidade(lista):
    print("\nNíveis de Sustentabilidade:")
    for item in lista:
        print(f"- {item}")
        

# Tela inicial do programa, com mensagem de boas-vindas e menu de opções
def Tela_principal():
    print(" ")
    print("BEM VINDO AO SUSTENTAÍ")
    print("")
    print("A sustentabilidade começa com pequenas escolhas diárias que fazem uma grande diferença no mundo. O Sustentaí é um projeto criado para inspirar e desafiar você a viver de forma mais sustentável.")
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+ Style.RESET_ALL)
    print(Fore.BLUE+"DESAFIO SUSTENTAÍ"+Style.BRIGHT)
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+ Style.RESET_ALL)
    print("Descubra seu nível de sustentabilidade! Participe do nosso desafio e descubra como suas ações impactam o planeta.")
    print("\n1. COMO FUNCIONA")
    print("2. COMEÇAR")
    print("3. CADASTRAR")

    opcao = input("\nDigite uma opção (1 - 2 ou 3): ")

    # Direciona para a função correta com base na escolha do usuário
    if opcao == "1":
        limpar_terminal()
        Exibir_como_funciona()
    elif opcao == "2":
        from tela_login import Tela_login
        limpar_terminal()
        Tela_login()
    elif opcao == "3":
        limpar_terminal()
        resposta = input(Fore.RED+"Deseja mesmo realizar um novo cadastro?(S/N): "+Style.RESET_ALL)
        
        if(resposta == "s" or resposta == "sim" or resposta == "SIM"):
            from tela_cadastro import Tela_cadastro
            Tela_cadastro()
        else:
            limpar_terminal()
            Tela_principal()
    else:
        print("Opção inválida. Tente novamente.")
        Tela_principal()  # Chama a função novamente para repetir o menu


# Explicação detalhada de como funciona o desafio de sustentabilidade
def Exibir_como_funciona():
    #linha amarela
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+ Style.RESET_ALL)
    print(Fore.BLUE+"COMO FUNCIONA:"+Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+ Style.RESET_ALL)
    print("O Desafio se baseia em 4 fases (Consumo de água, energia, resíduos e transporte)...")

    lista_sustentabilidade = criar_lista_sustentabilidade()
    exibir_lista_sustentabilidade(lista_sustentabilidade)

    input(Fore.GREEN+"\nPara voltar ao menu principal pressione Enter"+Style.RESET_ALL)
    limpar_terminal()
    Tela_principal()


# Exibe dicas práticas de sustentabilidade para o usuário
def Tela_de_dicas(usuario_logado):
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+ Style.RESET_ALL)
    print(Fore.BLUE+"TELA DE DICAS"+Style.BRIGHT)
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+ Style.RESET_ALL)
    print("\n  Dica 1: Reduza o consumo de plástico...")
    print("  Dica 2: Economize energia elétrica...")
    print("  Dica 3: Separe seu lixo para reciclagem")
    print("  Dica 4: Use mais transporte público")
    print("  Dica 5: Reveja seu consumo de água...")

    # Menu de navegação: ir para opções ou voltar ao menu principal
    while True: 
        print("\n1 - MENU DE OPÇÕES")
        print("2 - MENU PRINCIPAL")
        opcao20 = input("\nDigite a opção desejada: ")
        if opcao20 == "1":
            limpar_terminal()
            Tela_opcoes(usuario_logado)
        elif opcao20 == "2":
            limpar_terminal()
            from tela_menu import Tela_menu
            Tela_menu(usuario_logado)
        else:
            print("Opção inválida. Digite uma opção válida!")
            

# Tela final do programa, exibida ao usuário ao encerrar o desafio
def Tela_de_saida():
    #linha amarela
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+ Style.RESET_ALL)
    print("TELA DE SAÍDA")
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+ Style.RESET_ALL)
    print("\nParabéns por ter terminado nosso programa!")
    print("Esperamos que tenha gostado :)")
    print("Até a próxima!")
    print("\n**Esse programa foi idealizado e construído pelos alunos de engenharia de software, Grupo G7, da turma 103. PUC-Campinas.**")
    sys.exit()
