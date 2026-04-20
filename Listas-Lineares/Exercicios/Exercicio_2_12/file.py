"""
1. Busca

- Sequencial (Vetor): É a melhor (Muito rápido), Como o vetor guarda tudo em blocos contínuos de memória e você sabe o tamanho total, você pode usar a Busca Binária. É como procurar uma palavra no dicionário: você abre no meio, vê se a letra é maior ou menor, e descarta metade do livro de uma vez.

- Encadeada (Nós): É péssima para busca (Lento, precisa varrer elemento por elemento). Mesmo a lista estando em ordem alfabética, você não consegue "pular" para o meio dela, porque você só conhece o Sentinela e precisa perguntar de nó em nó quem é o próximo.

2. Inserção
- Sequencial (Vetor): Sofre muito (Lento devido ao deslocamento de memória). Para inserir o número "5" no início de um vetor ordenado de    1.000 posições, você tem que dar um laço for empurrando  1.000 elementos uma casa para a direita para abrir a vaga. 

- Encadeada (Nós): Instantâneo, independentemente do tamanho da lista uma vez que você achou o lugar (usando a busca), a inserção em si não move ninguém do lugar. Você apenas muda dois ponteiros.

3. Remoção

- Sequencial (Vetor): Mesmo problema da inserção. Se você remover o primeiro elemento, vai ficar um "buraco" no índice [0]. Você precisa fazer um for puxando todos os 999 elementos restantes uma casa para a esquerda

- Encadeada (Nós): Extremamente eficiente. Novamente, após achar o elemento, basta fazer o nó anterior "pular" o nó atual (ant.prox = pont.prox). Ninguém mais na lista fica sabendo que algo mudou.

Tabela de Comparação
_________________________________________________________________________________________________
Operação (Lista Ordenada) | Alocação Sequencial (Vetor) | Alocação Encadeada (Nós)  | Quem Vence?
-------------------------------------------------------------------------------------------------
Busca                     | Permite Busca Binária       | Busca estritamente linear | Sequencial 
Inserção                  | Exige deslocamento/Shift)   | Apenas troca de ponteiros | Encadeada Remoção                   | Exige deslocamento/Shift)   | Apenas troca de ponteiros | Encadeada

"""