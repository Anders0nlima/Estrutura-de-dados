# =========================
# POLINÔMIOS COM LISTA ENCADEADA
# =========================

class No:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.prox = None


class Polinomio:
    def __init__(self):
        self.ptlista = None

    # Inserção ordenada por expoente (decrescente)
    def inserir(self, coef, exp):
        novo = No(coef, exp)

        if self.ptlista is None or exp > self.ptlista.exp:
            novo.prox = self.ptlista
            self.ptlista = novo
            return

        atual = self.ptlista
        anterior = None

        while atual and atual.exp > exp:
            anterior = atual
            atual = atual.prox

        if atual and atual.exp == exp:
            atual.coef += coef
        else:
            novo.prox = atual
            anterior.prox = novo

    # Mostrar polinômio
    def mostrar(self):
        atual = self.ptlista
        termos = []

        while atual:
            termos.append(f"{atual.coef}x^{atual.exp}")
            atual = atual.prox

        print(" + ".join(termos) if termos else "0")

    # (i) Calcular P(x0)
    def calcular(self, x0):
        resultado = 0
        atual = self.ptlista

        while atual:
            resultado += atual.coef * (x0 ** atual.exp)
            atual = atual.prox

        return resultado

    # (ii) Soma de polinômios
    def somar(self, Q):
        p1 = self.ptlista
        p2 = Q.ptlista
        resultado = Polinomio()

        while p1 and p2:
            if p1.exp == p2.exp:
                resultado.inserir(p1.coef + p2.coef, p1.exp)
                p1 = p1.prox
                p2 = p2.prox
            elif p1.exp > p2.exp:
                resultado.inserir(p1.coef, p1.exp)
                p1 = p1.prox
            else:
                resultado.inserir(p2.coef, p2.exp)
                p2 = p2.prox

        while p1:
            resultado.inserir(p1.coef, p1.exp)
            p1 = p1.prox

        while p2:
            resultado.inserir(p2.coef, p2.exp)
            p2 = p2.prox

        return resultado

    # Função auxiliar para multiplicação
    def _inserir_ou_somar(self, coef, exp):
        if self.ptlista is None:
            self.ptlista = No(coef, exp)
            return

        atual = self.ptlista
        anterior = None

        while atual and atual.exp > exp:
            anterior = atual
            atual = atual.prox

        if atual and atual.exp == exp:
            atual.coef += coef
        else:
            novo = No(coef, exp)
            if anterior is None:
                novo.prox = self.ptlista
                self.ptlista = novo
            else:
                novo.prox = atual
                anterior.prox = novo

    # (iii) Multiplicação de polinômios
    def multiplicar(self, Q):
        resultado = Polinomio()

        p1 = self.ptlista
        while p1:
            p2 = Q.ptlista
            while p2:
                coef = p1.coef * p2.coef
                exp = p1.exp + p2.exp
                resultado._inserir_ou_somar(coef, exp)
                p2 = p2.prox
            p1 = p1.prox

        return resultado


# =========================
# TESTE
# =========================

P = Polinomio()
P.inserir(3, 2)
P.inserir(2, 1)
P.inserir(1, 0)

Q = Polinomio()
Q.inserir(1, 1)
Q.inserir(1, 0)

print("P(x):")
P.mostrar()

print("Q(x):")
Q.mostrar()

print("P(2):", P.calcular(2))

print("Soma P + Q:")
S = P.somar(Q)
S.mostrar()

print("Multiplicação P * Q:")
M = P.multiplicar(Q)
M.mostrar()