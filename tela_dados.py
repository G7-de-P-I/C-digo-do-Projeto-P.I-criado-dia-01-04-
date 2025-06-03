import os # para limpar terminal
from banco import conectar # para conectar BD e enviar corretamente
from colorama import Fore, Style # precisa de instalação local, serve para importar cores e destacar textos

# Função que limpa o terminal dependendo do sistema operacional
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Tela que mostra os dados do usuário logado (pontuação nos desafios)
def Tela_dados(usuario_logado, pontos1, pontos2, pontos3, pontos4):
        # Importa outras telas apenas quando essa função for chamada
        from tela_principal import Tela_de_dicas
        from tela_principal import Tela_de_saida
        from tela_desafios import Tela_opcoes
        
        # Conecta ao banco de dados
        conexao = conectar()
        cursor = conexao.cursor()
        
        # Comando para buscar as pontuações do usuário nos desafios
        comando = "SELECT pontuacao FROM respostas_desafios WHERE id_usuario = %s"
        cursor.execute(comando, (usuario_logado["id"],))  # Usa o ID do usuário logado
        resultado = cursor.fetchall()  # Pega todos os resultados retornados
        
        # Fecha a conexão com o banco
        cursor.close()
        conexao.close()

        # Soma os pontos de cada linha retornada
        desafios_diarios = [sum(linha) for linha in resultado]
        
        # Soma total dos pontos passados como parâmetro
        total_pontos = pontos1 + pontos2 + pontos3 + pontos4 

        # Calcula a porcentagem de cada desafio em relação ao total
        if total_pontos > 0:
            porcentagem1 = (pontos1 / total_pontos) * 100
            porcentagem2 = (pontos2 / total_pontos) * 100
            porcentagem3 = (pontos3 / total_pontos) * 100
            porcentagem4 = (pontos4 / total_pontos) * 100
        else:
            # Se não houver pontos, todas as porcentagens são zero
            porcentagem1 = porcentagem2 = porcentagem3 = porcentagem4 = 0
        
        # Título e informações da tela com cores
        print(Fore.LIGHTYELLOW_EX + "------------------------------------------------------------------" + Style.RESET_ALL)
        print(Fore.BLUE + "LEVANTAMENTO DE DADOS DIÁRIO" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "------------------------------------------------------------------" + Style.RESET_ALL)

        print("\nVamos ver detalhes da sua performance diária...")
        print("\nAgora você poderá saber o quão sustentável você é e onde pode melhorar, caso necessário!")
        print("Nível de sustentabilidade (diário) de acordo com cada desafio: ")

        # Mostra os pontos de cada desafio
        print(f"\nDesafio 1: {pontos1} pontos")
        print(f"Desafio 2: {pontos2} pontos")
        print(f"Desafio 3: {pontos3} pontos")
        print(f"Desafio 4: {pontos4} pontos")

        # Mostra a porcentagem de cada desafio
        print("\nDistribuição percentual dos pontos:")
        print(f"\nDesafio 1: {porcentagem1:.2f}%")
        print(f"Desafio 2: {porcentagem2:.2f}%")
        print(f"Desafio 3: {porcentagem3:.2f}%")
        print(f"Desafio 4: {porcentagem4:.2f}%")

        # Menu de opções
        while True:
            print("\nEscolha uma opção:")
            print("1 - MENU OPÇÕES")
            print("2 - OBTER DICAS")
            print("3 - FECHAR PROGRAMA")
            
            # Pede a escolha do usuário
            opcao9 = int(input("\nDigite a opção desejada: "))
        
            if opcao9 == 1:
                limpar_terminal()
                Tela_opcoes(usuario_logado)  # Vai para o menu de opções
            
            elif opcao9 == 2:
                limpar_terminal()
                Tela_de_dicas(usuario_logado)  # Vai para a tela de dicas
            
            elif opcao9 == 3:
                print("\nVocê encerrou o programa. Até mais!")
                limpar_terminal()
                Tela_de_saida()  # Finaliza o programa
            
            else:
                print("\nOpção inválida! Tente novamente.")  # Se digitar algo errado