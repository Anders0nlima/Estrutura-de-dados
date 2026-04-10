A grande vantagem de usar alocação encadeada para essas estruturas, em vez de vetores (alocação sequencial), é que você não precisa definir um tamanho máximo. A estrutura cresce e diminui dinamicamente na memória, evitando o erro de overflow (estouro de capacidade), a menos que a memória do próprio computador acabe.


## Pilhas (Stacks) em Alocação Encadeada
A Pilha segue a regra LIFO (Last In, First Out - O último a entrar é o primeiro a sair). Imagine uma pilha de pratos: você sempre coloca um prato novo no topo e, quando vai pegar um, tira do topo.

Na alocação encadeada, precisamos gerenciar apenas um ponteiro principal: o topo. Todas as operações (inserir e remover) acontecem exclusivamente nesse lado da lista.

### Algoritmo 2.18
Para inserir um novo elemento, adicionamos o nó sempre no início da lista (que chamamos de topo).

- ocupar(pt): Pede um espaço na memória para o novo nó e guarda a referência no ponteiro pt.
- pt^.info := novo-valor: Coloca o dado dentro desse novo nó.
- A mágica do encadeamento: pt^.prox := topo. O novo nó aponta para quem era o antigo topo da pilha.
- topo := pt: O ponteiro oficial topo da estrutura é atualizado para apontar para este novo nó, que agora é o "prato de cima".