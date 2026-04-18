# A remoção tem sempre 2 tempos:

# Encontrar o alvo: Chama a busca().
# A Ponte (Descostura): Pega o nó que vem antes do alvo e faz ele apontar para o nó que vem depois do alvo. O alvo fica isolado e o Python apaga ele da memória.

# A remoção é a arte de "pular" um nó.

class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None
        # self.ant = None (Se for dupla)

def busca(self, valor):
        # 1. Prepara o terreno (planta o valor no sentinela)
        self.ptlista.chave = valor 
        
        # 2. Posiciona os corredores no início
        ant = self.ptlista
        pont = self.ptlista.prox
        
        # 3. Caminha enquanto não achar
        while pont.chave != valor: # (Ou < valor, se for lista ordenada)
            ant = pont
            pont = pont.prox
            
        # 4. Retorna a dupla dinâmica!
        return ant, pont

#^^implementação anterior^^

def remover(self, valor):
        # 1. Encontra QUEM remover
        ant, pont = self.busca(valor)
        
        # 2. Verifica se achou um nó real (e não o sentinela)
        if pont != self.ptlista and pont.chave == valor:
            # 3. A Descostura: O de trás pula o atual e aponta pro da frente
            ant.prox = pont.prox 
        else:
            print("Valor não encontrado.")