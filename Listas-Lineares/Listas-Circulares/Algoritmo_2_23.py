class No:
    def __init__(self, chave=None):
        self.chave = chave
        self.prox = None
    
class ListaCircularOrdenada:
    def __init__(self):
        self.ptlista = No() # Nó cabeça (ptlista)
        self.ptlista.prox = self.ptlista
    
    def inserir_ordenado(self, valor):
        novo_no = No(valor)
        ant = self.ptlista
        pont = self.ptlista.prox

        #ate achar a posição certa ou da volta completa
        while pont != self.ptlista and pont.chave < valor:
            ant = pont
            pont = pont.prox
        
        # insere o novo nó entre 'ant' e 'pont'
        ant.prox = novo_no
        novo_no.prox = pont
    
    #algoritmo 2.23: busca 
    def buscar(self, x):
        ant = self.ptlista  # ant := ptlista

        #planta o valor buscado no nó cabeça
        self.ptlista.chave = x # ptlista^.chave := x

        pont = self.ptlista.prox # pont := ptlista^.prox

        while pont.chave < x: # enquanto pont^.chave < x faça
            ant = pont # ant := pont
            pont = pont.prox # pont := pont^.prox
        
        if pont != self.ptlista and pont.chave == x:
            print(f"-> Chave [{x}] localizada!")
            return pont # retorna o nó encontrado
        else:
            print(f"-> Chave [{x}] não localizada.")
            return None
    
    def imprimir(self):
        if self.ptlista.prox == self.ptlista:
            print("Lista vazia")
            return 
        
        pont = self.ptlista.prox
        saida = []
        while pont != self.ptlista:
            saida.append(str(pont.chave))
            pont = pont.prox
        print("Lista: (ptlista) -> " + " -> ".join(saida) + " -> (volta ao ptlista)")    
    
#teste

minha_lista = ListaCircularOrdenada()

minha_lista.inserir_ordenado(50)
minha_lista.inserir_ordenado(10)
minha_lista.inserir_ordenado(30)
minha_lista.inserir_ordenado(20)

minha_lista.imprimir()

print("Busca Realizando")
minha_lista.buscar(30)
minha_lista.buscar(10)
minha_lista.buscar(99)
minha_lista.buscar(15)