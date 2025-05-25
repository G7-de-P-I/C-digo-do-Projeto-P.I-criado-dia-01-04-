def Descriptografar_mensagem(texto_criptografado):
    # Alfabeto com '#' como 26
    alfabeto = 'abcdefghijklmnopqrstuvwxyz#'

    # Converte letra para número
    def letra_para_numero(letra):
        return ord(letra) - ord('a') if letra != '#' else 26

    # Converte número para letra
    def numero_para_letra(numero):
        return chr(numero + ord('a')) if numero < 26 else '#'

    # Multiplica bloco 2x1 pela matriz inversa 2x2
    def multiplicar_matriz(bloco, matriz):
        a, b = bloco  # Desempacota o vetor (bloco) nos valores a e b
        # Realiza a multiplicação de matrizes:
        # Aplica a operação módulo 27 ao resultado, comum em cifras como Hill Cipher
        x = (matriz[0][0] * a + matriz[0][1] * b) % 27
        y = (matriz[1][0] * a + matriz[1][1] * b) % 27

        return [x, y]  # Retorna o novo vetor transformado

    # Matriz inversa da chave [[5, 2], [3, 1]] mod 27
    matriz_inversa = [[26, 2], [3, 22]]

    # Converte texto em números
    numeros_cifrados = [letra_para_numero(c) for c in texto_criptografado]

    # Aplica a matriz inversa em blocos de 2
    texto_decifrado = ''
    # Inicia vazio
    for i in range(0, len(numeros_cifrados), 2):
        # Loop para operação, com range
        bloco = [numeros_cifrados[i], numeros_cifrados[i+1]]
        # Toma par de números
        decifrado = multiplicar_matriz(bloco, matriz_inversa)
        # Opera
        texto_decifrado += numero_para_letra(decifrado[0]) + numero_para_letra(decifrado[1])
        # Salva na variável do texto

    # Remove o '#' final se for padding
    if texto_decifrado.endswith('#'):
        texto_decifrado = texto_decifrado[:-1]

    return texto_decifrado

