#nesse tarefa e eu nao subdividi igual a tarefa 1, deixe como "algoritmo" a resolução inteira está nele

# tarefa 2
# Escreva um programa para implementar as duas funções de busca em lista ordenada apresentadas.
# Gere listas com números ordenados de diferentes tamanhos [1000-1000000].
# Para cada tamanho da lista compare o número de iterações de cada função de busca, considerando um valor aleatório a ser buscado.
# Plote um gráfico de linha para comparar o desempenho das duas funções.
# Disserte sobre os resultados observados e constru um relatório


import random
import matplotlib.pyplot as plt

# 1. Função de busca em lista ordenada (com sentinela)
def busca_ord(L, x):
    n = len(L)
    L.append(x)  # add no final da lista como sentinela
    i = 0
    iteracoes = 0
    
    while L[i] < x:
        iteracoes += 1
        i += 1
        
    L.pop()  # tira o sentinela para manter a lista normal
    
    # Verifica se encontrou ou se parou num valor maior (ou no fim da lista)
    if i == n or L[i] != x:
        return -1, iteracoes
    else:
        return i, iteracoes

# 2. Função de busca binária
def busca_bin(L, x):
    inf = 0
    sup = len(L) - 1
    iteracoes = 0
    
    while inf <= sup:
        iteracoes += 1
        meio = (inf + sup) // 2
        
        if L[meio] == x:
            return meio, iteracoes
        elif L[meio] < x:
            inf = meio + 1
        else:
            sup = meio - 1
            
    return -1, iteracoes

# 3. Preparação dos dados e testes
tamanhos = [1000, 10000, 100000, 500000, 1000000]
resultados_ord = []
resultados_bin = []

for t in tamanhos:
    # Gera uma lista ordenada.
    # Usamos saltos de 2 (0, 2, 4...) para permitir buscar números que não existem na lista
    lista_ordenada = list(range(0, t * 2, 2))
    
    # Escolhe um valor aleatório a ser buscado dentro do intervalo da lista
    x = random.randint(0, t * 2)
    
    _, it_ord = busca_ord(lista_ordenada, x)
    _, it_bin = busca_bin(lista_ordenada, x)
    
    resultados_ord.append(it_ord)
    resultados_bin.append(it_bin)
    
    print(f"Tamanho: {t:7d} | Iterações Ord: {it_ord:7d} | Iterações Bin: {it_bin:2d}")

# 4. Construção do Gráfico
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, resultados_ord, marker='o', color='red', label='Busca Ordenada (Sequencial)')
plt.plot(tamanhos, resultados_bin, marker='o', color='blue', label='Busca Binária')

plt.xlabel('Tamanho da Lista (N)')
plt.ylabel('Número de Iterações')
plt.title('Comparação de Desempenho: Busca Ordenada vs Busca Binária')
plt.legend()
plt.grid(True)
plt.show()

#para listas ordenadas, a Busca binária é superior. enquanto a busca sequencial sofre de um aumento drástico no custo computacional à medida que a lista cresce (crescimento linear), a busca binária demonstra uma escalabilidade exelente. Para grandes volumes de dados já estruturados, a Busca Binária é a escolha padrão e indispensável.