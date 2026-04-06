def busca(L, x):
    i = 0
    n = len(L)

    while i < n:  
        if L[i] == x:
            return i
        i += 1

    return -1

print(busca([10, 5, 34, 1, 2], 1))


# -> por que vai ser menos efeciente que o algoritimo_2_2.py?
# por causa do "while i < n:" e "if L[i] == x:" sao duas comparações, há um custo por repetições