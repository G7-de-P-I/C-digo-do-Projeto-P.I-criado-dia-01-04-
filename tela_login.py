import os
from banco import conectar  # Função para conectar ao banco de dados
from colorama import Fore, Style

# Limpa o terminal de acordo com o sistema operacional
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Tela de login do sistema
def Tela_login():
    print("----------------------------------------------------------------")
    print("LOGIN")
    print("----------------------------------------------------------------")
    print("")
    print("Olá! Para começarmos nosso desafio, precisamos te conhecer!")

    while True:
        try:
            resposta = input("Possui cadastro?(SIM/NÃO): ")
            
            # Se a pessoa já tiver cadastro, segue para o login
            if(resposta == "SIM" or resposta == "sim" or resposta == "Sim"):

                while True:
                    email = input("\nDigite seu email: ")
                    senha = input("Digite sua senha: ")

                    conexao = None
                    cursor = None 

                    try:
                        # Conecta ao banco e cria um cursor para fazer consultas
                        conexao = conectar()
                        cursor = conexao.cursor(dictionary=True)

                        # Consulta para verificar se o email e senha existem no banco
                        comando = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
                        valores = (email, senha)
                        cursor.execute(comando, valores)
                        usuario_logado = cursor.fetchone()  # Retorna os dados do usuário se encontrado

                        # Se as credenciais forem válidas, avança para o menu
                        if usuario_logado:
                            from tela_menu import Tela_menu
                            print("\n✅ Login realizado com sucesso!")
                            input(Fore.GREEN+"Pressione Enter para continuar..."+Style.RESET_ALL)
                            limpar_terminal()
                            Tela_menu(usuario_logado)
                            break
                        else:
                            print("\n❌ Email ou senha incorretos!")
                            input(Fore.RED+"Pressione Enter para tentar novamente..."+Style.RESET_ALL)

                    except Exception as e:
                        print(f"\n⚠️ Erro ao fazer login: {e}")
                    
                    # Fecha o cursor e a conexão com o banco de dados, se existirem
                    finally:
                        if cursor:
                            cursor.close()
                        if conexao:
                            conexao.close()

            # Se não tiver cadastro, redireciona para a tela de cadastro
            else:
                from tela_cadastro import Tela_cadastro
                limpar_terminal()
                print(Fore.LIGHTYELLOW_EX+"\n----------------------------------------------------------------"+Style.RESET_ALL)
                print("REALIZE SEU CADASTRO PRIMEIRO")
                Tela_cadastro()

        except ValueError as e:
            print(e)
            print(Fore.RED+"Tente Novamente")
