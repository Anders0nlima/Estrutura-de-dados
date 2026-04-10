
#algoritmo 2.14
class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.ptlista = None

    #algoritmo 2.15
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


    # Como a lista é apenas encadeada em uma direção (singly linked list), se quisermos inserir ou remover um elemento no meio dela, precisaremos sempre saber quem é o elemento anterior a ele.

    # Por isso, sua função de busca não retorna apenas se achou ou não. Ela encontra o ponteiro do elemento procurado (pont) E o ponteiro do elemento que vem antes dele (ant).


    #algoritmo 2.16
    def inserir(self, x):
        ant, pont = self.busca_enc(x)

        if pont is None: # so insere se nao existir na tabela
            novo_no = No(x) #ocupar(pt) e enicializar nó

            #caso especial: inserindo no INÍCIO da lista (vazia ou menor elemento)
            if ant is None:
                novo_no.prox = self.ptlista
                self.ptlista = novo_no
            else:
                #inserindo no meio ou no fim
                novo_no.prox = ant.prox #aponta para o proximo do anterior
                ant.prox = novo_no
            print(f"Elemento {x} inserido.")
        else:
            print(f"Elemento {x} já está na tabela")



    #algoritmo 2.17
    def remover(self, x):
        ant, pont = self.busca_enc(x)

        if pont is not None: # o elemento existe na tebela
            if ant is None:
                #caso especial: o elemento a ser removido é o primeiro da lista
                self.ptlista = pont.prox
            else:
                #removendo do meio ou do fim
                ant.prox = pont.prox # o anterior pula o nó removido

            print(f"Elemento {x} removido com sucesso")
        else:
            print("Nó não se encontra na tabela")

    #Impressao para podemos testar

    def imprimir(self):
        pont = self.ptlista
        saida = []
        while pont is not None:
            saida.append(str(pont.chave))
            pont = pont.prox
        print("Lista: [" + " -> ".join(saida) + " -> None]")


# Teste

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