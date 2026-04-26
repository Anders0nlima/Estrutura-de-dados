def eh_palindromo(palavra):
    pilha = []

    # 1. Empilhar todos os caracteres
    for letra in palavra:
        pilha.append(letra)

    # 2. Comparar com a palavra original
    for letra in palavra:
        topo = pilha.pop()

        if letra != topo:
            return False

    return True


print(eh_palindromo("raiar"))  # True
print(eh_palindromo("ovo"))    # True
print(eh_palindromo("casa"))   # False