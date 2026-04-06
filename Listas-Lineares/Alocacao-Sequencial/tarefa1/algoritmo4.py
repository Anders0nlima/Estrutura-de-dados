#Para cada tamanho da lista compare o número de iterações de cada função de 
#busca, considerando o mesmo valor a ser buscado

# Função de busca normal
def busca(L, x):
    i = 0
    n = len(L)
    interacoes = 0

    while i < n:  
        interacoes += 1
        if L[i] == x:
            return i, interacoes
        i += 1

    return -1, interacoes


# Função de busca com sentinela
def busca_sentinela(L, x):
    n = len(L)
    L.append(x)
    i = 0
    interacoes = 0

    while L[i] != x:
        interacoes += 1
        i += 1
    
    L.pop() 

    if i < n:
        return i, interacoes
    else:
        return -1, interacoes


# Gerador de lista aleatória
import random

def num_aleatorio(n):
    lista = []

    for i in range(n):
        numero = random.randint(1, 1000000)
        lista.append(numero)
    
    return lista


# Teste com diferentes tamanhos
tamanhos = [1000, 10000, 100000, 1000000]

for t in tamanhos:
    lista = num_aleatorio(t)

    # mesmo valor para as duas buscas
    x = lista[-1]  # pior caso

    _, it1 = busca(lista.copy(), x)
    _, it2 = busca_sentinela(lista.copy(), x)

    print(f"\nTamanho da lista: {t}")
    print(f"Busca normal - Iterações: {it1}")
    print(f"Busca com sentinela - Iterações: {it2}")