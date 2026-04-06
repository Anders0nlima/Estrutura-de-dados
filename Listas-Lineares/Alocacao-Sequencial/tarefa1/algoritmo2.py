def busca_sentinela(L, x):
    n = len(L)
    L.append(x)
    i = 0

    while L[i] != x:
        i += 1
    
    L.pop() 

    if i < n:
        return i
    else:
        return -1


print(busca_sentinela([10, 5, 34, 3, 2], 1))