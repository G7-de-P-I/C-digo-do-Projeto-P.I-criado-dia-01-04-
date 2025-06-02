import os
from banco import conectar
from colorama import Fore, Style

def limpar_terminal():
    # Limpa o terminal, funciona tanto no Windows (cls) quanto em sistemas Unix (clear)
    os.system('cls' if os.name == 'nt' else 'clear')


# Função para mostrar a tela de sustentabilidade mensal para o usuário logado
def Tela_mensal(usuario_logado):
    from datetime import date
    from tela_desafios import Tela_opcoes
    from criptografia import Criptografar_Mensagem
    from descriptografia import Descriptografar_mensagem

    # Exibe um cabeçalho colorido com o título da tela
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
    print(Fore.BLUE+"SUSTENTABILIDADE MENSAL"+Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)

    # Conecta ao banco de dados e cria um cursor para executar comandos SQL
    conexao = conectar()
    cursor = conexao.cursor()
    id_usuario = usuario_logado["id"]

    # Verifica se já existe um resultado mensal salvo para o usuário no mês e ano atual
    comando_verificar_existente = """
                SELECT 1 FROM resultados_desafios
                WHERE id_usuario = %s AND EXTRACT(YEAR FROM data) = %s AND EXTRACT(MONTH FROM data) = %s
                LIMIT 1
            """
    hoje = date.today()
    cursor.execute(comando_verificar_existente, (id_usuario, hoje.year, hoje.month))
    resultado_existente = cursor.fetchone()

    # Verifica quantos dias distintos o usuário respondeu desafios e soma as pontuações
    comando_verificar_dias = """
                            SELECT
                                COUNT(DISTINCT DATE(data_resposta)) AS total_dias,
                                SUM(pontuacao) AS soma_total
                            FROM respostas_desafios
                            WHERE id_usuario = %s;
                            """
    cursor.execute(comando_verificar_dias, (id_usuario,))
    quantidade_registros = cursor.fetchone()

    # Consulta a mensagem criptografada do resultado mensal do usuário no banco
    comando_mensagem_criptografada = """SELECT resultado_mensal from resultados_desafios 
                                        WHERE id_usuario = %s;"""
    cursor.execute(comando_mensagem_criptografada, (id_usuario,))
    resultado = cursor.fetchone()

    # Se existir mensagem criptografada, descriptografa para mostrar ao usuário
    if resultado[0]:
        mensagem_criptografada = resultado[0]
        descriptografada = Descriptografar_mensagem(mensagem_criptografada)
    else:
        descriptografada = "Sem dados"

    # Pega a soma das pontuações acumuladas nos desafios
    pontuacao_mes = quantidade_registros[1]

    # Calcula a média mensal dividindo a pontuação por 30 dias
    Smensal = float(pontuacao_mes) / 30

    # Define o nível de sustentabilidade baseado na média mensal
    if 30 <= Smensal <= 40:
        nivel = "ALTA"
        criptografado = Criptografar_Mensagem(nivel)
    elif 20 <= Smensal < 30:
        nivel = "MODERADA"
        criptografado = Criptografar_Mensagem(nivel)
    else:
        nivel = "BAIXA"
        criptografado = Criptografar_Mensagem(nivel)

    # Se já existe resultado no banco para o mês atual, mostra o nível descriptografado
    if resultado_existente:
        print(f"Sua média de pontos mensal foi: {Smensal:.2f}")
        print(f"NÍVEL DE SUSTENTABILIDADE MENSAL: {descriptografada}!\n")
        print("\nA média funciona em função de 30 dias, \nfaça esses desafios ao longo deste período e \nentão quem sabe não recebe um pontuação maior!!!")

    else:
        # Se ainda não existe resultado salvo, mostra o nível calculado e salva no banco
        print(f"Sua média de pontos mensal foi: {Smensal:.2f}")
        print(f"NÍVEL DE SUSTENTABILIDADE MENSAL: {nivel}!\n")

        comando_inserir = """
                INSERT INTO resultados_desafios (id_usuario, resultado_mensal, data)
                VALUES (%s, %s, %s)
                """
        data_atual = date.today()
        cursor.execute(comando_inserir, (id_usuario, criptografado, data_atual))
        conexao.commit()

    # Fecha o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()

    # Menu simples para o usuário escolher continuar no menu ou sair do programa
    while True:
        print("----------------------------------------------------------------------")
        print("Escolha uma opção:")
        print("1 - MENU DE OPÇÕES")
        print("2 - FECHAR PROGRAMA")
        print("----------------------------------------------------------------------")
        opcao = input("Digite a opção desejada:")

        if opcao == "1":
            limpar_terminal()
            Tela_opcoes(usuario_logado)  # Retorna para o menu principal
            break

        elif opcao == "2":
            limpar_terminal()
            print("\nAté mais!")  # Encerra o programa
            break

        else:
            print("Opção inválida. Tente novamente.")  # Validação simples de entrada inválida
