import random

def num_aleatorio(n):
    lista = []

    for i in range(n):
        numero = random.randint(1, 1000000)
        lista.append(numero)
    
    return lista

tamanho = [1000, 10000, 100000, 1000000]

for t in tamanho:
    lista = num_aleatorio(t)
    print(f"lista com {t} elementos criados")
    print(num_aleatorio(t))

#print(num_aleatorio(5))