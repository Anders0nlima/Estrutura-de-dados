### Conceito
- Uma Lista Circular é muito parecida com a lista encadeada simples, mas com uma diferença crucial: o último nó não aponta para nulo/vazio ($\lambda$). Ele aponta de volta para o primeiro nó da lista. Isso cria um ciclo (um loop fechado).
- Na Figura 2.9, podemos notar um bloco sombreado no início chamado ptlista. Ele é o que chamamos de Nó Cabeça (ou Sentinela). Ele não guarda um dado real da sua aplicação; ele serve apenas como um ponto de partida fixo para a estrutura. O último nó ($z$) aponta de volta para esse nó cabeça.

### diferença

- Pilha (LIFO): Você só mexe no topo.

- Fila (FIFO): Você entra no fim e sai no início.

- Lista Ordenada: Você insere o elemento em uma posição específica baseada no valor dele (a "chave"), não importa a ordem de chegada. Além disso, a busca pode acontecer em qualquer lugar da lista.