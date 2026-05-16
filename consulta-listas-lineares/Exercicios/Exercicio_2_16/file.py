"""
2.16 Seja L uma lista simplesmente encadeada, composta dos números l1, l2, …, ln, respectivamente, segundo a ordem de armazenamento. Escrever um algoritmo que, percorrendo L uma única vez, constrói uma outra lista L', formada dos elementos seguintes: 
(i) l2, l3, …, ln, l1;
(ii) ln, ln - 1, …, l1;   
(iii) l1 + ln, l2 + ln - 1, …, ln/2 + ln/2+1, onde n é par. 
"""
class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None

class Lista:
    def __init__(self):
        self.ptlista = No(None)
        self.ptlista.prox = None

    def inserir(self, valor):
        novo = No(valor)
        novo.prox = self.ptlista.prox
        self.ptlista.prox = novo

    def mostrar(self):
        atual = self.ptlista.prox
        while atual:
            print(atual.chave, end=" → ")
            atual = atual.prox
        print("None")

    def construir_listas(self):
        atual = self.ptlista.prox

        L_rot = Lista()
        L_inv = Lista()
        L_soma = Lista()

        valores = []

        while atual:
            valores.append(atual.chave)
            L_inv.inserir(atual.chave) 
            atual = atual.prox

        n = len(valores)
        if n == 0:
            return L_rot, L_inv, L_soma
        
        L_rot.inserir(valores[0])
        for i in range(n - 1, 0, -1):
            L_rot.inserir(valores[i])

        if n % 2 == 0:
            meio = n // 2
            for i in range(meio - 1, -1, -1):
                j = n - 1 - i  # O espelho de 'i' no final do array
                soma = valores[i] + valores[j]
                L_soma.inserir(soma)

        return L_rot, L_inv, L_soma

l = Lista()

l.inserir(4)
l.inserir(3)
l.inserir(2)
l.inserir(1)

print("Original (Esperado: 1 -> 2 -> 3 -> 4):")
l.mostrar()
rot, inv, soma = l.construir_listas()
print("Rotação (Esperado: 2 -> 3 -> 4 -> 1):")
rot.mostrar()
print("Inverso (Esperado: 4 -> 3 -> 2 -> 1):")
inv.mostrar()
print("Soma (Esperado: 5 -> 5):")
soma.mostrar()