# A busca é o coração de tudo, Quase toda inserção e remoção em listas ordenadas dependem de uma busca prévia para saber onde agir.

# O padrão é sempre um laço while que caminha usando pont = pont.prox até bater no valor desejado ou no fim da lista.

# Retorna o ponteiro encontrado (e às vezes o anterior, se não for lista dupla).

# O objetivo é andar na lista até achar o valor ou bater no sentinela.

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