def criar_lista_sustentabilidade():
    """Cria uma lista dos níveis de sustentabilidade."""

    sustentabilidade = [
        "Alta: 30 - 40  (10pts)",
        "Moderada: 20 - 29 (5pts)",
        "Baixa: 8 - 19  (2pts)"
    ]
    return sustentabilidade

def exibir_lista_sustentabilidade(lista):
    """Exibe a lista de sustentabilidade."""

    print("Níveis de Sustentabilidade:")
    for item in lista:
        print(f"- {item}")

def tela_boas_vindas():
    """Exibe a tela de boas-vindas e processa a entrada do usuário."""
    print(" ")
    print("BEM VINDO AO SUSTENTAÍ")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("A sustentabilidade começa com pequenas escolhas diárias que fazem uma grande diferença no mundo. O Sustentaí é um projeto criado para inspirar e desafiar você a viver de forma mais sustentável.")

    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Desafio Sustentaí")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Descubra seu nível de sustentabilidade! Participe do nosso desafio e descubra como suas ações impactam o planeta. A cada passo, você aprende, evolui e contribui para um futuro mais verde e consciente. Está pronto para fazer a diferença? Vamos juntos nessa jornada sustentável!")
    print("\n1. Como funciona")
    print("2. Começar")

    opcao = input("\nDigite uma opção (1 ou 2): ")

    if opcao == "1":
        exibir_como_funciona()
    elif opcao == "2":
        tela_login()
    else:
        print("Opção inválida. Tente novamente.")
        tela_boas_vindas()  # Chama a função novamente para repetir o processo

def exibir_como_funciona():
    """Exibe o texto explicando como o Sustentaí funciona."""

    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Como funciona:")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("O Desafio se baseia em 4 fases (Consumo de água, energia, resíduos e transporte). Para cada fase há uma classificação podendo ser (Alta, Moderada e Baixa Sustentabilidade), com uma determinada pontuação para cada (Alta = 10; Moderada = 5; Baixa = 2). Ao final do Desafio diário somaremos cada classificação de cada fase, obtendo uma pontuação que determinará seu nível total de sustentabilidade. Observe abaixo a ponderação para seu nível total de sustentabilidade:")
    print(" ")

    
    lista_sustentabilidade = criar_lista_sustentabilidade()
    exibir_lista_sustentabilidade(lista_sustentabilidade)

    input("\nPara voltar ao menu principal pressione Enter")
    tela_boas_vindas()

def tela_login():
    

    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Login")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Olá! Para começarmos nosso desafio, precisamos te conhecer!")
    usuario = input("\nDigite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    # login
    print(f"\nUsuário: {usuario}")
    print(f"Senha: {senha}")
    print("Login realizado com sucesso!")
    input("\nPara continuar pressione Enter")
    tela_boas_vindas()

# Inicia o programa
tela_boas_vindas()