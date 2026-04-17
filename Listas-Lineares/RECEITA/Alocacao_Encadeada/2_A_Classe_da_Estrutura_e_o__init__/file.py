class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None
        # self.ant = None (Se for dupla)

#^^implementação anterior^^


class MinhaEstrutura:
    def __init__(self):
        self.ptlista = No(None) # Exemplo com sentinela
        self.ptlista.prox = self.ptlista



# Muda o quê?
# Lista: Tem o ptlista (sentinela ou cabeça).
# Pilha: O marcador se chama topo.
# Fila: Você precisa de dois marcadores: inicio e fim.