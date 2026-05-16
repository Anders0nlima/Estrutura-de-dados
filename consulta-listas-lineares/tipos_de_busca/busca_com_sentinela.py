def busca_sentinela(L, x):
    n = len(L)
    L.append(x) # -> em py quando eu adiciono algo na lista ele vai para o final automaticamente
    i = 0

    while L[i] != x:
        i += 1
    
    L.pop() # -> quando ele acha o x ele remove o sentilena (o pop sempre remove o ultimo da lista)

    if i < n:
        return i
    else:
        return -1
    
print(busca_sentinela([10, 5, 34, 3, 2], 1))