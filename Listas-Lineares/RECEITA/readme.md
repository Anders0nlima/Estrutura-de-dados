## como a receita se adapta apenas mudando as restrições:

### 1. Pilhas (Stacks - LIFO)
Regra: O último a entrar é o primeiro a sair.

A Receita: Você deleta o Passo 3 (Busca). Você não pode buscar no meio de uma pilha.

Inserção (push): Insere sempre no topo. O novo_no.prox vira o topo antigo, e o topo passa a ser o novo_no.

Remoção (pop): Tira sempre do topo. O topo passa a ser o topo.prox.

### 2. Filas (Queues - FIFO)
Regra: O primeiro a entrar é o primeiro a sair.

A Receita: Também não tem busca no meio.

Inserção (enqueue): Insere sempre no marcador fim.

Remoção (dequeue): Remove sempre do marcador inicio.

### 3. Listas Lineares (Simples, Duplas, Circulares)
Regra: Entra onde quiser (ou ordenado), sai de onde quiser.

A Receita: Usa a receita completa (Passos 1 a 5). A circularidade e o duplo encadeamento só mudam a quantidade de ponteiros que você "costura" e "descostura" no Passo 4 e 5.

## E a Alocação Sequencial?
Na Alocação Sequencial (a primeira parte do sumário), é só trocar os ponteiros (prox, ant) por Índices de um Vetor ([0], [1], [i+1]).

Em vez de "costurar", a inserção no meio da lista te obriga a fazer um "for" empurrando todo mundo uma casa para a direita para abrir espaço. A remoção te obriga a fazer um "for" puxando todo mundo uma casa para a esquerda para tapar o buraco. (Foi por isso que usamos o Vetor Circular no Deque, para fugir desse "empurra-empurra"!).