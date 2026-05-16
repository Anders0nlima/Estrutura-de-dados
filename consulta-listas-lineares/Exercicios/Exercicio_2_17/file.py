"""
2.17 Uma palavra é um palíndromo se a sequência de letras que a forma é a mesma, quer seja lida da esquerda para a direita ou da direita para a esquerda (exemplo: raiar). Escrever um algoritmo eficiente para reconhecer se uma dada palavra é um palíndromo. Escolher a estrutura de dados conveniente para representar a palavra. 
"""
def eh_palindromo(palavra):
    pilha = []
    for letra in palavra:
        pilha.append(letra)

    for letra in palavra:
        topo = pilha.pop()

        if letra != topo:
            return False

    return True

print(eh_palindromo("raiar"))  # True
print(eh_palindromo("ovo"))    # True
print(eh_palindromo("casa"))   # False