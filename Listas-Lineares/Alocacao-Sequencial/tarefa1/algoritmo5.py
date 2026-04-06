#Plote um gráfico de linha para comparar o desempenho das duas funções.
#○ Disserte sobre os resultados observados e constru um relatório

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


# montagem do gráfico
import matplotlib.pyplot as plt

tamanhos = [1000, 10000, 100000, 1000000]

resultados_busca = []
resultados_sentinela = []

for t in tamanhos:
    lista = num_aleatorio(t)

    x = lista[-1]  # pior caso

    _, it1 = busca(lista.copy(), x)
    _, it2 = busca_sentinela(lista.copy(), x)

    resultados_busca.append(it1)
    resultados_sentinela.append(it2)


# gráfico
plt.plot(tamanhos, resultados_busca, marker='o', label='Busca Normal')
plt.plot(tamanhos, resultados_sentinela, marker='o', label='Busca com Sentinela')

plt.xlabel('Tamanho da Lista')
plt.ylabel('Número de Iterações')
plt.title('Comparação de Desempenho das Buscas')

plt.legend()
plt.grid()

plt.show()