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

# -> caso nao tenha o x ele vai contar o sentinela no final em vez de i = 4 ele vai ser i = 5 (com sentinela) nesse caso nao vai obedecer isso "if i < n:" pois o n representa o tamanho da lista e caso o i ultrapasse (contando com o sentinela) ele vai retorna -1 
