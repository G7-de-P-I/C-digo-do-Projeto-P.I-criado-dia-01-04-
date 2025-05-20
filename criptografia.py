def Criptografar_Mensagem(mensagem):
    # Alfabeto usado (a-z + '#')
    alfabeto = 'abcdefghijklmnopqrstuvwxyz#'

    # Converte letra para número
    def letra_para_numero(letra):
        return 26 if letra == '#' else ord(letra) - ord('a')

    # Converte número para letra
    def numero_para_letra(numero):
        return '#' if numero == 26 else chr(numero + ord('a'))

    # Limpa o texto: deixa só letras do alfabeto
    def limpar_texto(texto):
        texto = texto.lower()
        return ''.join(c for c in texto if c in alfabeto)

    # Multiplica matriz 2x2 com bloco de 2 números
    def multiplicar_matriz(bloco, matriz):
        a, b = bloco
        x = (matriz[0][0] * a + matriz[0][1] * b) % 27
        y = (matriz[1][0] * a + matriz[1][1] * b) % 27
        return [x, y]

    # Matriz-chave da cifra de Hill
    chave = [[5, 2], [3, 1]]

    # Limpa o texto
    texto_limpo = limpar_texto(mensagem)

    # Adiciona '#' se tiver número ímpar de letras
    if len(texto_limpo) % 2 != 0:
        texto_limpo += '#'

    # Converte letras para números
    numeros = [letra_para_numero(c) for c in texto_limpo]

    # Criptografa em blocos de 2
    resultado = ''
    for i in range(0, len(numeros), 2):
        bloco = [numeros[i], numeros[i+1]]
        cifrado = multiplicar_matriz(bloco, chave)
        resultado += numero_para_letra(cifrado[0]) + numero_para_letra(cifrado[1])

    return resultado

