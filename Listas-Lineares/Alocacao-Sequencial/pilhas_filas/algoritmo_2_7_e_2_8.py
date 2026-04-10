M = 5 # capacidade da pilha
P = [None] * M # nossa memoria fisica, com tamanho fixo de 5 
topo = -1 # significa que a pilha tá vazia 

def inserir_pilha(P, topo, M, novo_valor):
    if topo < M - 1: # aqui vamos ate o indice 4, [0, 1, 2, 3, 4] 
        topo += 1 # add
        P[topo] = novo_valor
        print(f"Pilha (Push): {novo_valor} inserido no índice {topo}.")
    else:
        print("Pilha (Overflow): pilha cheia")
    return topo

def remover_pilha(P, topo):
    if topo >= 0:
        valor_recuperado = P[topo]
        P[topo] = None
        topo -= 1
        print(f"Pilha (Pop): {valor_recuperado} removido.")
    else:
        print("Pilha (Underflow): A pilha já está vazia!")
    return topo

topo = inserir_pilha(P, topo, M, 13)
topo = inserir_pilha(P, topo, M, 22)
topo = inserir_pilha(P, topo, M, 90)

topo = remover_pilha(P, topo)


# demostrações
print(f"Estado final da memória: {P}")
print(f"Topo atual: {topo}")