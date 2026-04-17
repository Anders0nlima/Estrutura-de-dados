# A lógica da inserção tem sempre 3 tempos:

# 1. Encontrar o local: Chama a função busca() (ou vai direto pro topo/fim se for Pilha/Fila).
# 2. Criar o Nó: Instancia novo_no = No(valor).
# 3. A Dança dos Ponteiros (Costura): Conecta o braço direito do novo_no, depois conecta quem estava atrás dele. A ordem importa para não "perder" o resto da lista!