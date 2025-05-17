import os
from banco import conectar
from colorama import Fore, Style

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função para a tela de sustentabilidade mensal
def Tela_mensal(usuario_logado):
    from datetime import date
    from tela_desafios import Tela_opcoes


    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
    print(Fore.BLUE+"SUSTENTABILIDADE MENSAL"+Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)

 # Conectar ao banco
    conexao = conectar()
    cursor = conexao.cursor()
    id_usuario = usuario_logado["id"]

    # Verificar quantos registros mensais já existem para esse usuário
    comando_verificar_dias = """
                            SELECT
                                COUNT(DISTINCT DATE(data_resposta)) AS total_dias,
                                SUM(pontuacao) AS soma_total
                            FROM respostas_desafios
                            WHERE id_usuario = %s;
                            """
                            
    cursor.execute(comando_verificar_dias, (id_usuario,))
    quantidade_registros = cursor.fetchone()
    
    #pega o resultado de dias que tem de registros
    total_dias = quantidade_registros[0]
    #pega a soma dos registros feito no período de 30 dias
    pontuacao_mes = quantidade_registros[1]
    


    # Só continua se tiver 30 respostas
    if total_dias == 30:
        # Calcular média mensal
            Smensal = sum(pontuacao_mes) / 30

    # Mostrar nível (opcional)
            if 30 <= Smensal <= 40:
                nivel = "ALTA"
            elif 20 <= Smensal < 30:
                nivel = "MODERADA"
            else:
                nivel = "BAIXA"

            print(f"Sua média de pontos mensal foi: {Smensal:.2f}")
            print(f"NÍVEL DE SUSTENTABILIDADE MENSAL: {nivel}!\n")

    # Inserir na tabela de resultados mensais
            comando_inserir = """
            INSERT INTO resultados_desafios (id_usuario, resultado_mensal, data)
            VALUES (%s, %s, %s)
            """
            data_atual = date.today()
            cursor.execute(comando_inserir, (id_usuario, nivel, data_atual))
            conexao.commit()
    else:
            print(Fore.RED+"Ainda não há 30 dias de resultados ou já foi registrado um resultado mensal."+Style.RESET_ALL)

    # Fechar conexão
    cursor.close()
    conexao.close()

    # Menu de opções
    while True:
        print("----------------------------------------------------------------------")
        print("Escolha uma opção:")
        print("1 - MENU DE OPÇÕES")
        print("2 - FECHAR PROGRAMA")
        print("----------------------------------------------------------------------")
        opcao = input("Digite a opção desejada: ")


        if opcao == "1":
            limpar_terminal()
            Tela_opcoes(usuario_logado)
            break

        elif opcao == "2":
            limpar_terminal()
            print("\nAté mais!")
            
            break

        else:
            print("Opção inválida. Tente novamente.")
            