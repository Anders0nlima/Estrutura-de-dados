#Melhor para entender(facil de implementar)

class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None
    
class ListaNaoOrdenada:
    def __init__(self):
        self.ptlista = No(None)
        self.ptlista.prox = None # nao aponta para ele mesmo dessa vez (marca o fim da linha)
    
    def busca(self, valor):
        ant = self.ptlista
        pont = self.ptlista.prox

        # Continua enquanto não chegar no fim (None) E não achar o valor
        while pont is not None and pont.chave != valor:
            ant = pont
            pont = pont.prox
        return ant, pont
    
    def inserir(self, valor):
        novo_no = No(valor)
        novo_no.prox = self.ptlista.prox
        self.ptlista.prox = novo_no
    
    def remover(self, valor):
        ant, pont = self.busca(valor)

        if pont is not None:
            ant.prox = pont.prox 
        else:
            print("Valor nao encontrado na lista")
