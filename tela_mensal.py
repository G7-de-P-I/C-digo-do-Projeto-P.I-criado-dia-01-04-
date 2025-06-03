import os
from banco import conectar
from colorama import Fore, Style

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função para a tela de sustentabilidade mensal
def Tela_mensal(usuario_logado):
    from datetime import date
    from tela_desafios import Tela_opcoes
    from criptografia import Criptografar_Mensagem
    from descriptografia import Descriptografar_mensagem
    



    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)
    print(Fore.BLUE+"SUSTENTABILIDADE MENSAL"+Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX+"------------------------------------------------------------------"+Style.RESET_ALL)

 # Conectar ao banco
    conexao = conectar()
    cursor = conexao.cursor()
    id_usuario = usuario_logado["id"]
    
    
    comando_verificar_existente = """
                SELECT 1 FROM resultados_desafios
                WHERE id_usuario = %s AND EXTRACT(YEAR FROM data) = %s AND EXTRACT(MONTH FROM data) = %s
                LIMIT 1
            """
    hoje = date.today()
    cursor.execute(comando_verificar_existente, (id_usuario, hoje.year, hoje.month))
    resultado_existente = cursor.fetchone()


#==============================================================================================

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


    comando_mensagem_criptografada = """SELECT resultado_mensal from resultados_desafios 
                                        WHERE id_usuario = %s;"""
                                        
    cursor.execute(comando_mensagem_criptografada, (id_usuario,))
    resultado = cursor.fetchone()
    
    if resultado and  resultado[0]:
        mensagem_criptografada = resultado[0]
        descriptografada = Descriptografar_mensagem(mensagem_criptografada)
    else:
        descriptografada = "Sem dados"


    #pega a soma dos registros feito no período de 30 dias
    pontuacao_mes = quantidade_registros[1]
        
    # Calcular média mensal
    Smensal = float(pontuacao_mes) / 30

        # Mostrar nível
    if 30 <= Smensal <= 40:
            nivel = "ALTA"
            criptografado = Criptografar_Mensagem(nivel)
            
    elif 20 <= Smensal < 30:
            nivel = "MODERADA"
            criptografado = Criptografar_Mensagem(nivel)
    else:
            nivel = "BAIXA"
            criptografado = Criptografar_Mensagem(nivel)
    
    
    if resultado_existente:
        
        
        print(f"Sua média de pontos mensal foi: {Smensal:.2f}")
        print(f"NÍVEL DE SUSTENTABILIDADE MENSAL: {descriptografada}!\n")
        print("\nA média funciona em função de 30 dias, \nfaça esses desafios ao longo deste período e \nentão quem sabe não recebe um pontuação maior!!!")
        
    else:

        print(f"Sua média de pontos mensal foi: {Smensal:.2f}")
        print(f"NÍVEL DE SUSTENTABILIDADE MENSAL: {nivel}!\n")

        # Inserir na tabela de resultados mensais
        comando_inserir = """
                INSERT INTO resultados_desafios (id_usuario, resultado_mensal, data)
                VALUES (%s, %s, %s)
                """
                
        data_atual = date.today()
        cursor.execute(comando_inserir, (id_usuario, criptografado, data_atual))
        conexao.commit()

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
            