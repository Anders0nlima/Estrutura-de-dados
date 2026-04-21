"""
objetivo alternar entre as lintas
L1: 1 → 3 → 5
L2: 2 → 4 → 6 → 8

saida:
L1: 1 → 2 → 3 → 4 → 5 → 6
L2: 8 -> sobra
"""
class No:
    def __init__(self, chave):
        self.chave = chave 
        self.prox = None

class ListaNaoOrdenada:
    def __init__(self):
        self.ptlista = No(None)
        self.ptlista.prox = None

    def inserir(self, valor):
        novo = No(valor)
        novo.prox = self.ptlista.prox
        self.ptlista.prox = novo

    def mostrar(self):
        atual = self.ptlista.prox
        elementos = []

        while atual is not None:
            elementos.append(str(atual.chave))
            atual = atual.prox

        print(" → ".join(elementos))

    def intercalar(self, lista2):
        p1 = self.ptlista.prox
        p2 = lista2.ptlista.prox

        while p1 is not None and p2 is not None:
            prox1 = p1.prox
            prox2 = p2.prox

            p1.prox = p2
            p2.prox = prox1

            p1 = prox1
            p2 = prox2

        # restante da lista2 (se sobrar)
        lista2.ptlista.prox = p2

l1 = ListaNaoOrdenada()
l2 = ListaNaoOrdenada()

l1.inserir(5)
l1.inserir(3)
l1.inserir(1)

l2.inserir(6)
l2.inserir(4)
l2.inserir(2)

print("Lista 1:")
l1.mostrar()

print("Lista 2:")
l2.mostrar()

# Intercalar
l1.intercalar(l2)

print("Após intercalar:")
l1.mostrar()

print("Resto da lista 2:")
l2.mostrar()
