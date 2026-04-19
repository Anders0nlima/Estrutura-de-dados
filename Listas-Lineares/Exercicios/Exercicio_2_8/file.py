class No:
    def __init__(self, chave):
        self.chave = chave 
        self.prox = None
    
class CircularEncadeada:
    def __init__(self):
        self.ptlista = No(None)
        self.ptlista.prox = self.ptlista

    def busca(self, valor):
        self.ptlista.chave = valor  
        ant = self.ptlista
        pont = self.ptlista.prox

        while pont.chave < valor:
            ant = pont
            pont = pont.prox
        
        return ant, pont
    
    def inserir(self, valor):
        self.ptlista.chave = valor
        ant, pont = self.busca(valor)

        novo_no = No(valor)

        novo_no.prox = pont
        ant.prox = novo_no
    
    def remover(self, valor):
        ant, pont = self.busca(valor)

        if pont != self.ptlista and pont.chave == valor:
            ant.prox = pont.prox
        else: 
            print("Valor nao encontrado")





