"""
2.6 Apresentar algoritmos para um deque em alocação sequencial. São dados fornecidos: na inserção: o nó a ser inserido e a extremidade desejada (E1 ou E2), na remoção: a extremidade da remoção. 
Deque (Double-Ended Queue) é uma "Fila de Duas Pontas", (no Deque você pode inserir e remover de ambos os lados da fila - Diferente da fila comum, onde você só entra por um lado e sai pelo outro).
Pseudocodigos:
"Inserção pela Extremidade 1 (E1): Como colocar um novo elemento no "início" do vetor?"
"Inserção pela Extremidade 2 (E2): Como colocar um novo elemento no "fim" do vetor?"
"Remoção pela Extremidade 1 (E1): Como tirar quem está no "início"?"
"Remoção pela Extremidade 2 (E2): Como tirar quem está no "fim"?"
"""
class DequeSequancial():
    def __init__(self, N):
        self.N = N  # capacidade maxima
        self.dados = [None] * N # lugar onde vamos por os numeros 
        self.inicio = 0 # em vez de "ptlista", usamos dois índices para marcar as pontas.
        self.fim = 0
        self.tamanho = 0 # para saber se a lista está vazia ou cheia
# Inserção - E1 ou E2
    def inserir(self, x, extremidade):
        if self.tamanho == self.N: # tamanho está igual a capacidade maxima?
            print("Overflow") 
            return
        if extremidade == 1: # E1 (Esquerda/Início)
            self.inicio = (self.inicio - 1 + self.N) % self.N # N=5|inicio=0 -> (0-1+5)MOD5 = 4
            self.dados[self.inicio] = x # self.dados[4] -> indice o valor "x" para para o indice 4
        else: # E2 (Direita/Fim)
            self.dados[self.fim] = x # guarda
            self.fim = (self.fim + 1) % self.N
        
        self.tamanho += 1
# Remoção - E1 ou E2
    def remover(self, extremidade):
        if self.tamanho == 0:
            print("Erro, Underflow")
            return
        if extremidade == 1: # E1 (Tira do Início)
            valor = self.dados[self.inicio]
            self.inicio = (self.inicio + 1) % self.N
        else: # E2 (Tira do Fim)
            self.fim = (self.fim - 1 + self.N) % self.N
            valor = self.dados[self.fim]
        
        self.tamanho -= 1
        return valor

# TESTANDO
deque = DequeSequancial(5)

deque.inserir(10, 2) # inserir o valor 10 com E2 dados = [[10], [none], [none], [none], [none]]
deque.inserir(20, 2) # inserir o valor 20 com E2 dados = [[10], [20], [none], [none], [none]]
deque.inserir(5, 1)  # inicio = (0 - 1 + 5) % 5 = 4
                     # dados = [[10], [20], [none], [none], [5]]
deque.inserir(1, 1)  # inicio = (4 - 1 + 5) % 5 = 3
                     # dados = [[10], [20], [none], [1], [5]]
deque.remover(1)     # dados = [[10], [20], [none], [none], [5]]