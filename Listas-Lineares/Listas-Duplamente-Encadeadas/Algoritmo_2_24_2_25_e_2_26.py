# note: O uso simultâneo de duplo encadeamento + circularidade + sentinela é considerado o "estado da arte" em listas ligadas básicas, pois você elimina todos aqueles ifs de verificar se a lista está vazia, se está inserindo no começo, ou se chegou no final. O anel resolve tudo sozinho!


class No:
    def __init__(self, chave=None):
        self.chave = chave 
        self.ant = None
        self.prox = None
    
class ListaDuplaCircular:
    def __init__(self):
        self.ptlista = No() # sentinela (nó cabeça)
        # na lista vazia, o sentinela aponta para si mesmo nos dois sentidos
        self.ptlista.prox = self.ptlista
        self.ptlista.prox = self.ptlista
        self.ptlista.ant = self.ptlista
    
    # algoritmo 2.24: busca
    def busca(self, x):
        #planta o valor no sentinela
        self.ptlista.chave = x
        pont = self.ptlista.prox

        #percorre a lista para frente
        while pont.chave < x:
            pont = pont.prox
        
        # retorna o nó onde a busca parou
        return pont
    
    #algoritmo 2.25: inserção
    def inserir(self, x):
        pont = self.busca(x)

        #verifica se o elemnto ja existe
        if pont != self.ptlista and pont.chave == x:
            print(f"Erro: O elemento [{x}] já existe na lista.")
            return
        
        #ocupar(pt) e inicializar
        novo_no = No(x)

        # as 4 conexões vitais da figura 2.12
        novo_no.prox = pont           # 1
        novo_no.ant = pont.ant        # 2
        pont.ant.prox = novo_no       # 3
        pont.ant = novo_no            # 4

        print(f"Elmento [{x}] inserido")

    #algoritmo 2.26: remoção
    def remover(self, x):
        pont = self.busca(x)

        #remove so se encontrar
        if pont != self.ptlista and pont.chave == x:
            pont.ant.prox = pont.prox
            pont.prox.ant = pont.ant
            print(f"Elemento [{x}] removido")
        else:
            print(f"Erro: o elemento [{x}] não se encontra na lista")
        
    def imprimir(self):
        if self.ptlista.prox == self.ptlista:
            print("Lista vazia.")
            return

        pont = self.ptlista.prox
        saida = []
        while pont != self.ptlista:
            saida.append(str(pont.chave))
            pont = pont.prox
            
        print("Lista: (sentinela) <=> " + " <=> ".join(saida) + " <=> (volta)")

# teste 
lista_dupla = ListaDuplaCircular()

print("--- Inserções ---")
lista_dupla.inserir(30)
lista_dupla.inserir(10)
lista_dupla.inserir(40)
lista_dupla.inserir(20)
lista_dupla.inserir(20) # Tentativa de inserir duplicado
lista_dupla.imprimir()

print("\n--- Remoções ---")
lista_dupla.remover(30) # Removendo do meio
lista_dupla.remover(10) # Removendo do início (logo após sentinela)
lista_dupla.remover(99) # Tentativa de remover inexistente
lista_dupla.imprimir()



