# Reutilizando a estrutura de Nó e FilaEncadeada que ja fizemos
class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir(self, valor):
        novo_no = No(valor)
        if self.fim:
            self.fim.prox = novo_no
        else:
            self.inicio = novo_no
        self.fim = novo_no

    def remover(self):
        if not self.inicio: return None
        valor = self.inicio.valor
        self.inicio = self.inicio.prox
        if not self.inicio: self.fim = None
        return valor

    def esta_vazia(self):
        return self.inicio is None

def ordenacao_distribuicao(lista, num_digitos):
    # Criamos 10 filas (uma para cada dígito de 0 a 9 na base 10)
    baldes = [FilaEncadeada() for _ in range(10)]
    
    # Processa cada dígito (i=0 para unidade, i=1 para dezena...)
    for i in range(num_digitos):
        # 1. DISTRIBUIÇÃO (Baseado na primeira parte do Algoritmo 2.22)
        for num in lista:
            # Extrai o i-ésimo dígito
            digito = (num // (10**i)) % 10
            baldes[digito].inserir(num)
        
        # 2. COLETA (Baseado na segunda parte do Algoritmo 2.22)
        indice_lista = 0
        for k in range(10):
            while not baldes[k].esta_vazia():
                lista[indice_lista] = baldes[k].remover()
                indice_lista += 1
                
    return lista

# teste
numeros = [170, 45, 75, 90, 802, 24, 2, 66]
# O maior número é 802, então num_digitos = 3
resultado = ordenacao_distribuicao(numeros, 3)
print(f"Lista Ordenada: {resultado}")