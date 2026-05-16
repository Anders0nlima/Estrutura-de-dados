#algoritmo 2.14
class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.ptlista = None

    def busca_enc(self, x):
        ant = None
        pont = None
        ptr = self.ptlista  # ponteiro de percurso

        while ptr is not None:
            if ptr.chave < x:
                ant = ptr  # atualiza o anterior
                ptr = ptr.prox # avança o atual
            elif ptr.chave == x:
                pont = ptr  # chave encontrada!
                ptr = None # Força a saída do while (ptr := lambda)
            else:
                ptr = None # elemento não existe

        return ant, pont

    def inserir(self, x):
        ant, pont = self.busca_enc(x)

        if pont is None: # so insere se nao existir na tabela
            novo_no = No(x) #ocupar(pt) e enicializar nó

            if ant is None:
                novo_no.prox = self.ptlista
                self.ptlista = novo_no
            else:
                novo_no.prox = ant.prox #aponta para o proximo do anterior
                ant.prox = novo_no
            print(f"Elemento {x} inserido.")
        else:
            print(f"Elemento {x} já está na tabela")

    def remover(self, x):
        ant, pont = self.busca_enc(x)

        if pont is not None: # o elemento existe na tebela
            if ant is None:
                self.ptlista = pont.prox
            else:
                ant.prox = pont.prox # o anterior pula o nó removido

            print(f"Elemento {x} removido com sucesso")
        else:
            print("Nó não se encontra na tabela")

    def imprimir(self):
        pont = self.ptlista
        saida = []
        while pont is not None:
            saida.append(str(pont.chave))
            pont = pont.prox
        print("Lista: [" + " -> ".join(saida) + " -> None]")

lista = ListaEncadeada()

print("Inserindo")
lista.inserir(10)
lista.inserir(5)
lista.inserir(20)
lista.inserir(25)

lista.imprimir()

print("Removendo")
lista.remover(25)
lista.imprimir()
lista.remover(5)
lista.imprimir()