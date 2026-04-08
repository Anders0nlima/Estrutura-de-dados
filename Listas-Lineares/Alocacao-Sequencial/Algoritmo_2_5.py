def busca(L, n, x):
    for i in range(n):
        if L[i] == x:
            return i
    return -1

#n -> numero len atual 
#M -> capacidade maxima da lista
def inserir(L, n, M, novo_valor):
    if n < M:
        if busca(L, n, novo_valor) == -1:
            L[n] = novo_valor
            n += 1
            print(f"Inserido: {novo_valor}")
        else:
            print("elemento ja existe na tabela")
    else:
        print("Overflow: tabela cheia")
    
    return n


print(inserir([10, 20, 30, 40, 50, None], 4, 5, 60))



#ate o 2_6 quero tentar fazer algo mais facil, antes de pilha e fila 
