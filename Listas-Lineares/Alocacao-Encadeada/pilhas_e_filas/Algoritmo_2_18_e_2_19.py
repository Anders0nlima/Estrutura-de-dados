class No:
    def __init__(self, valor):
        self.valor = valor # equivalente ao 'info' no algotitmo
        self.prox = None # ponteiro para o proximo nó
    
class PilhaEncadeada:
    def __init__(self):
        self.topo = None
    
    #algoritmo 2.18: inserção na pilha
    def inserir(self, novo_valor):
        novo_no = No(novo_valor) # ocupar(pt) e pt^.info := novo-valor

        novo_no.prox = self.topo # pt^.prox := topo
        self.topo = novo_no # topo := pt
        print(f"[{novo_valor}] inserido no topo da pilha")
    
    #algoritmo 2.19: remoção de pilha
    def remover(self):
        if self.topo is not None: # se topo != lambda
            pt = self.topo # pt := topo
            self.topo = self.topo.prox # topo := topo^.prox

            valor_recuperado = pt.valor # recupera o valor
            # O Python tem "Garbage Collector", então não precisamos de um
            # comando explícito como "desocupar(pt)", a memória é limpa sozinha.

            print(f"[{valor_recuperado}] removido do topo da pilha")
            return valor_recuperado
        else: 
            print("Underflow: pilha vazia")
            return None
    def imprimir(self):
        pont = self.topo
        saida = []
        while pont is not None:
            saida.append(str(pont.valor))
            pont = pont.prox
        print("Pilha (topo -> base): [" + " -> ".join(saida) + " -> None]")


print("teste")
minha_pilha = PilhaEncadeada()
minha_pilha.inserir(10)
minha_pilha.inserir(20)
minha_pilha.inserir(30)
minha_pilha.imprimir

minha_pilha.remover() #remove o 30
minha_pilha.imprimir()