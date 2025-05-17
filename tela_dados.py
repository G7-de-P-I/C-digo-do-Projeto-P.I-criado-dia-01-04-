import os
from banco import conectar
from colorama import Fore, Style 

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Tela_dados(usuario_logado, pontos1, pontos2, pontos3, pontos4):
        from tela_principal import Tela_de_dicas
        from tela_principal import Tela_de_saida
        from tela_desafios import Tela_opcoes
        
        conexao = conectar()
        cursor = conexao.cursor()
    
        comando = "SELECT pontuacao FROM respostas_desafios WHERE id_usuario = %s"
    
        cursor.execute(comando, (usuario_logado["id"],))
        resultado = cursor.fetchall()
    
        cursor.close()
        conexao.close()

        
        desafios_diarios = [sum(linha) for linha in resultado]
        
        total_pontos = pontos1 + pontos2 + pontos3 + pontos4 
        if total_pontos > 0:
            porcentagem1 = (pontos1 / total_pontos) * 100
            porcentagem2 = (pontos2 / total_pontos) * 100
            porcentagem3 = (pontos3 / total_pontos) * 100
            porcentagem4 = (pontos4 / total_pontos) * 100
        else:
            porcentagem1 = porcentagem2 = porcentagem3 = porcentagem4 = 0
        
        print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
        print(Fore.BLUE+"LEVANTAMENTO DE DADOS DIÁRIO"+Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
        print("\nVamos ver detalhes da sua performance diária...")
        print("\nAgora você poderá saber o quão sustentável você é e onde pode melhorar, caso necessário!")
        print("Nível de sustentabilidade (diário) de acordo com cada desafio: ")
        
        print(f"\nDesafio 1: {pontos1} pontos")
        print(f"Desafio 2: {pontos2} pontos")
        print(f"Desafio 3: {pontos3} pontos")
        print(f"Desafio 4: {pontos4} pontos")
        print("\nDistribuição percentual dos pontos:")
        
        print(f"\nDesafio 1: {porcentagem1:.2f}%")
        print(f"Desafio 2: {porcentagem2:.2f}%")
        print(f"Desafio 3: {porcentagem3:.2f}%")
        print(f"Desafio 4: {porcentagem4:.2f}%")
        
        while True:
            print("\nEscolha uma opção:")
            print("1 - MENU OPCÕES")
            print("2 - OBTER DICAS")
            print("3 - FECHAR PROGRAMA")
            opcao9 = int(input("\nDigite a opção desejada: "))
        
            if opcao9 == 1:
                limpar_terminal()
                Tela_opcoes(usuario_logado)
            
            elif opcao9==2:
                limpar_terminal()
                Tela_de_dicas(usuario_logado)
            
            elif opcao9==3:
                print("\nVocê encerrou o programa. Até mais!")
                limpar_terminal()
                Tela_de_saida()
            
            else:
                print("\nOpção inválida! Tente novamente.")
