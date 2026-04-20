class No:
    def __init__(self, chave, info=None):
        self.chave = chave
        self.info = info
        self.prox = None

class CircularEncadeada:
    def __init__(self):
        self.ptlista = No(None)
        self.ptlista.prox = self.ptlista

    # adaptação para busca, inserir e remover para lidar com a 'info' extra
    def busca(self, valor_chave):
        self.ptlista.chave = valor_chave
        ant = self.ptlista
        pont = self.ptlista.prox

        while pont != self.ptlista and pont.chave < valor_chave:
            ant = pont
            pont = pont.prox
        return ant, pont
    
    def inserir(self, chave, info=None):
        ant, pont = self.busca(chave)
        novo_no = No(chave, info)
        novo_no.prox = pont
        ant.prox = novo_no

    def remover(self, chave):
        ant, pont = self.busca(chave)

        if pont != self.ptlista and pont.chave == chave:
            ant.prox = pont.prox
        else: 
            print("Valor nao encontrado")

    # --- Resposta da Questão 2.9 ---
    def alterar_info(self, chave_busca, nova_info):
        ant, pont = self.busca(chave_busca)
        if pont != self.ptlista and pont.chave == chave_busca:
            pont.info = nova_info
        else:
            print("Chave não encontrada")


    # --- Resposta da Questão 2.10 ---
    def alterar_chave(self, chave_antiga, nova_chave):
        ant, pont = self.busca(chave_antiga)
        if pont != self.ptlista and pont.chave == chave_antiga:
            info_salva = pont.info
            self.remover(chave_antiga)
            self.inserir(nova_chave, info_salva)
        else:
            print("Chave antiga não encontrada")
    
    def mostrar(self):
        atual = self.ptlista.prox
        elementos = []

        while atual != self.ptlista:
            elementos.append(f"({atual.chave}, {atual.info})")
            atual = atual.prox

        print(" → ".join(elementos))

lista = CircularEncadeada()

# Inserindo
lista.inserir(10, "A")
lista.inserir(20, "B")
lista.inserir(30, "C")

print("Inicial:")
lista.mostrar()

# Alterar info é editar, alterar chave é reconstruir
# info=None → campo opcional
# alterar_info → muda conteúdo
# alterar_chave → remove e reinsere
# busca → encontra posição
# nserir → conecta nós
# remover → pula o nó