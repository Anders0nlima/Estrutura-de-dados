# codigo bom para revisão


class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None

class ListaOrdenada:
    def __init__(self):
        self.ptlista = No(None)
        self.ptlista.prox = None
    
    def inserir(self, valor):
        ant = self.ptlista
        pont = self.ptlista.prox

        while pont is not None and pont.chave < valor:
            ant = pont
            pont = pont.prox
        
        novo = No(valor)
        novo.prox = pont
        ant.prox = novo
    
    def mostrar(self):
        atual = self.ptlista.prox
        while atual is not None:
            print(atual.chave, end =" -> ")
            atual = atual.prox
        print("None")
    
    def intercalar_ordenado(self, lista2):
        p1 = self.ptlista.prox
        p2 = lista2.ptlista.prox
        ant = self.ptlista

        while p1 is not None and p2 is not None:
            if p1.chave <= p2.chave:
                ant.prox = p1
                p1 = p1.prox
            else:
                ant.prox = p2
                p2 = p2.prox
            
            ant = ant.prox 
        
        if p1 is not None:
            ant.prox = p1
        else:
            ant.prox = p2
        
        lista2.ptlista.prox = p2

l1 = ListaOrdenada()
l2 = ListaOrdenada()

l1.inserir(1)
l1.inserir(3)
l1.inserir(5)

l2.inserir(2)
l2.inserir(4)
l2.inserir(6)

print("Lista 1:")
l1.mostrar()

print("Lista 2:")
l2.mostrar()

l1.intercalar_ordenado(l2) #L2

print("Resultado:")
l1.mostrar()

