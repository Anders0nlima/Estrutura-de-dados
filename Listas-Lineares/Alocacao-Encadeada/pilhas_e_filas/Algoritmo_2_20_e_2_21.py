class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    #algoritmo 2.20
    def inserir(self, novo_valor):
        novo_no = No(novo_valor)

        if self.fim is not None: # se fim != lambda
            self.fim.prox = novo_no # fim^.prox := pt
        else:
            self.inicio = novo_no # inicio := pt (fila estava vazia)
        
        self.fim = novo_no #fim := pt
        print(f"[{novo_valor}] inserido no fim da lista")


    #algoritmo 2.21
    def remover(self):
        if self.inicio is not None: 
            pt = self.inicio # pt := inicio
            self.inicio = self.inicio.prox #inicio := inicio^.prox

            if self.inicio is None: #se inicio = lambda
                self.fim = None # fim := lambda (fila ficou vazia)
            
            valor_recuperado = pt.valor
            print(f"[{valor_recuperado}] removido do inicio da fila")
            return valor_recuperado
        else:
            print("underflow: fila vazia")
            return None
    
    def imprimir(self):
        pont = self.inicio
        saida = []
        while pont is not None:
            saida.append(str(pont.valor))
            pont = pont.prox
        print("Fila (Inicio -> Fim): [" + " -> ".join(saida) + " -> None]")


print("teste")
minha_fila = FilaEncadeada()
minha_fila.inserir(10)
minha_fila.inserir(20)
minha_fila.inserir(30)
minha_fila.imprimir()

minha_fila.remover() # deve remover o 10
minha_fila.imprimir()
