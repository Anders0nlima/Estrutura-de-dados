def busca_bin(L, x):
    inf = 0
    sup = len(L) - 1 

    while inf <= sup:
        meio = (inf + sup) // 2

        if L[meio] == x:
            return meio
        elif L[meio] < x:
            inf = meio + 1
        else:
            sup = meio - 1

    return -1


print(busca_bin([1, 2, 3, 4, 5], 4))

