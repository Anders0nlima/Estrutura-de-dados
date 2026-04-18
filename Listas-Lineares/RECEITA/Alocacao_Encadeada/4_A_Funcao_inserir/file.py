# A lógica da inserção tem sempre 3 tempos:

# 1. Encontrar o local: Chama a função busca() (ou vai direto pro topo/fim se for Pilha/Fila).
# 2. Criar o Nó: Instancia novo_no = No(valor).
# 3. A Dança dos Ponteiros (Costura): Conecta o braço direito do novo_no, depois conecta quem estava atrás dele. A ordem importa para não "perder" o resto da lista!

# O segredo da inserção é a ordem das ligações. O novo nó sempre segura a lista primeiro, para depois a lista segurar ele.


class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None
        # self.ant = None (Se for dupla)

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

#^^implementação anterior^^

def inserir(self, valor):
        # 1. Encontra ONDE inserir
        ant, pont = self.busca(valor) 
        
        # 2. Cria o novo nó
        novo_no = No(valor)
        
        # 3. Costura (A dança dos ponteiros)
        novo_no.prox = pont  # Braço direito do novo nó segura o da frente
        ant.prox = novo_no   # Quem estava atrás solta o 'pont' e segura o novo nó