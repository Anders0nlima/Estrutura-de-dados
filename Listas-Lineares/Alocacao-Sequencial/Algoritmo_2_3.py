def busca_ord(L, x):
    n = len(L)
    L.append(x)
    i = 0

    while L[i] < x:
        i += 1
    
    L.pop()

    if i == n or L[i] != x: # sentinela
        return -1
    else:
        return i

print(busca_ord([1, 4, 2, 3, 5], 4))

    

