# Lista Duplamente Encadeada
As listas simples têm um problema crônico: você só consegue andar para frente. Se você estiver no nó 50 e quiser voltar para o nó 49, você não pode; precisa começar a busca toda de novo a partir do início da lista.

### Na Figura 2.10 e 2.11
- O nó sombreado é o sentinela (ptlista). Ele não guarda dados úteis.
- O primeiro nó real (com chave $K_1$) tem seu ant apontando para o sentinela.
- O último nó real (com chave $K_n$) tem seu prox apontando para o sentinela.
- O ant do sentinela aponta para o último nó, e o prox do sentinela aponta para o primeiro.

- Isso cria um anel perfeito que pode ser percorrido em qualquer direção!

### Busca (Algoritmo 2.24)
- Como a lista é ordenada e usa um sentinela, a busca é quase idêntica à da lista circular de antes.

- O truque de colocar ptlista^.chave := x continua aqui.

- A diferença é que a função não precisa mais retornar o ponteiro ant (anterior) e o pont (atual). Ela só retorna o pont.

- Por que? Porque se você tem o pont, você automaticamente tem o anterior acessando pont^.ant! Isso simplifica muito.

### Inserção (Figura 2.12 e Algoritmo 2.25)
o que percebemos foi uma "dança dos ponteiros" que é necessária para inserir um novo nó ($pt$) sem quebrar a lista.
Como cada nó tem dois braços, precisamos fazer quatro conexões ao invés de duas. O algoritmo sempre insere o novo nó antes do ponteiro pont encontrado na busca.

#### Os 4 passos do algoritmo são:
- pt^.prox := pont: O braço direito do novo nó segura o nó atual.

- pt^.ant := pont^.ant: O braço esquerdo do novo nó segura o que antes era o anterior do nó atual.

- pont^.ant^.prox := pt: O vizinho da esquerda solta o nó atual e passa a apontar seu braço direito para o novo nó.

- pont^.ant := pt: O nó atual passa a apontar seu braço esquerdo para o novo nó.

### Remoção (Figura 2.13 e Algoritmo 2.26)
como "isolar" o nó que queremos remover (pont). É a operação mais elegante de todas, pois precisamos de apenas duas linhas de código para costurar a lista por cima do nó removido:

- pont^.ant^.prox := pont^.prox: O vizinho da esquerda do nó removido passa a apontar direto para o vizinho da direita.

- pont^.prox^.ant := pont^.ant: O vizinho da direita do nó removido passa a apontar direto para o vizinho da esquerda.

O nó pont fica completamente isolado e é limpo da memória.