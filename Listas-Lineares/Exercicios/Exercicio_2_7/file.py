M = 5
P = [None] * M
topo1 = -1 # começo da pilha 1
topo2 = M # começo da pilha 2

# duas pilhas compartilhando a mesma memoria
def inserir_p2(P, topo1, topo2, novo_valor):
    if topo2 - 1 > topo1:
        topo2 -= 1
        P[topo2] = novo_valor
        print(f"Valor inserido na P2: {novo_valor} no indice {topo2}")
    else:
        print(f"pilha cheia na P2")
    return topo2
    
def inserir_p1(P, topo1, topo2, novo_valor):
    if topo1 + 1 < topo2:
        topo1 += 1
        P[topo1] = novo_valor
        print(f"Valor inserido na P1: {novo_valor} no indice {topo1}")
    else:
        print("pilha cheia na P1")
    return topo1

def remover_p2(P, topo2):
    if topo2 < M:
        valor_recuperado = P[topo2]
        P[topo2] = None
        topo2 += 1
        print(f"Valor removido na P2: {valor_recuperado}")
    else:
        print("Pilha vazia na P2")
    return topo2

def remover_p1(P, topo1):
    if topo1 >= 0:
        valor_recuperado = P[topo1]
        P[topo1] = None
        topo1 -= 1
        print(f"Valor removido na P1: {valor_recuperado}")
    else:
        print("Pilha vazia na P1")
    return topo1


# Inserindo na P1
topo1 = inserir_p1(P, topo1, topo2, 10)
topo1 = inserir_p1(P, topo1, topo2, 20)

# Inserindo na P2 (ela vai ocupar os índices 4 e 3)
topo2 = inserir_p2(P, topo1, topo2, 99)
topo2 = inserir_p2(P, topo1, topo2, 88)

topo2 = remover_p2(P, topo2)

print(f"Vetor P: {P}")






