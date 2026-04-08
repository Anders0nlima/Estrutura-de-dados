def busca(L, n, x):
    for i in range(n):
        if L[i] == x:
            return i
    return -1

def remover(L, n, x):
    if n != 0:
        indice = busca(L, n, x)

        if indice != -1:
            for i in range(indice, n - 1):
                L[i] = L[i + 1]
            
            L[n-1] = None
            n -= 1
            print(f"Elemento {x} removido")
        else:
            print("Elemento nao se encontra na tebela")
    else:
        print("Underflow: tabela vazia")
    
    return n


print(remover([1, 2, 3, 4, 5], 5, 2))