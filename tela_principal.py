import mysql.connector
import sys
from rich.console import Console
from rich.table import Table
from datetime import datetime
from tela_desafios import Tela_desafio, Tela_de_nivel_diario
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')





pontos1=10
pontos2=10
pontos3=10
pontos4=10



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
        
        

def Tela_principal():

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
        limpar_terminal()
        Exibir_como_funciona()
    elif opcao == "2":
        from tela_login import Tela_login
        limpar_terminal()
        Tela_login()
    elif opcao == "3":
        limpar_terminal()
        from tela_cadastro import Tela_cadastro
        Tela_cadastro()
    else:
        print("Opção inválida. Tente novamente.")
        Tela_principal()  # Chama a funÃ§Ã£o novamente para repetir o processo



def Exibir_como_funciona():

    
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
    limpar_terminal()
    Tela_principal()
            
def Tela_de_dicas():
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
        print("Digite para continuar: (1) Tela de Nível ou (2) Menu Principal")
        print("")
        opcao20= input("Digite a opção desejada: ")
        if opcao20=="1":
            limpar_terminal()
            Tela_de_nivel_diario()
        elif opcao20=="2":
            limpar_terminal()
            from tela_menu import Tela_menu
            Tela_menu()
        else:
            print("Opção inválida. Digite uma opção válida!")
            
    #tela de saída e dicas

def Tela_de_saida():
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
            
    
def Tela_perfil():
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
    limpar_terminal()
    from tela_menu import Tela_menu
    Tela_menu()