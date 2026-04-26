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

    # Nome corrigido!
    def construir_listas(self):
        atual = self.ptlista.prox

        L_rot = Lista()
        L_inv = Lista()
        L_soma = Lista()

        valores = []

        # 1. A ÚNICA PASSADA NOS PONTEIROS DE L
        while atual:
            valores.append(atual.chave)
            
            # Dica Ninja: O seu 'inserir' já inverte a ordem naturalmente!
            # Se você for inserindo enquanto varre a lista, a L_inv se constrói sozinha.
            L_inv.inserir(atual.chave)
            
            atual = atual.prox

        n = len(valores)
        if n == 0:
            return L_rot, L_inv, L_soma

        # 2. CONSTRUINDO A ROTAÇÃO (i)
        # Queremos a ordem: l2, l3, ..., ln, l1
        # Como o 'inserir' coloca no início, nós o alimentamos de trás para frente!
        # Inserimos l1 primeiro, e depois ln, ln-1, ..., l2
        L_rot.inserir(valores[0])
        for i in range(n - 1, 0, -1):
            L_rot.inserir(valores[i])

        # 3. CONSTRUINDO A SOMA (iii)
        # Queremos os pares das pontas para o centro.
        # Alimentamos do centro para as pontas!
        if n % 2 == 0:
            meio = n // 2
            for i in range(meio - 1, -1, -1):
                j = n - 1 - i  # O espelho de 'i' no final do array
                soma = valores[i] + valores[j]
                L_soma.inserir(soma)

        return L_rot, L_inv, L_soma


# --- TESTE ---
l = Lista()

# Para a lista original ficar 1 -> 2 -> 3 -> 4, 
# temos que inserir do 4 até o 1 (por causa do seu 'inserir' no início)
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