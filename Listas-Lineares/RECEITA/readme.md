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
- Nota: Aqui não temos a classe "No" individual, os "ingredientes" são o próprio vetor e o seu tamanho máximo.

Em vez de "costurar", a inserção no meio da lista te obriga a fazer um "for" empurrando todo mundo uma casa para a direita para abrir espaço. A remoção te obriga a fazer um "for" puxando todo mundo uma casa para a esquerda para tapar o buraco. (Foi por isso que usamos o Vetor Circular no Deque, para fugir desse "empurra-empurra"!).

### Como transformamos essa Lista Simples em uma Pilha (Stack - LIFO)?
A regra da Pilha é: Só insere no topo, só remove do topo.

apaga a função busca() inteira.

Inserção Adaptada: Ao invés de usar ant, pont = self.busca(), tem que "travar" os ponteiros no início. O ant sempre será o Sentinela (ptlista) e o pont sempre será o primeiro elemento (ptlista.prox).

Remoção Adaptada: Mesma coisa, não busca. O ant é o sentinela e o pont é o primeiro elemento. É só dar o comando de "pular" o primeiro nó: self.ptlista.prox = self.ptlista.prox.prox.

### E para uma Fila (Queue - FIFO)?
A regra é: Insere no fim, remove no começo.

Apaga a busca de novo.

Inserção Adaptada: cria um ponteiro extra chamado fim que fica parado no último nó. Para inserir, você liga o novo nó no fim e atualiza quem é o novo fim.

Remoção Adaptada: Exatamente igual à da Pilha (tira do começo).

## SOBRE PONTOS (.)
por que tantos pontos? em 2.8 e outros
```
class No:
    def __init__(self, chave):
        self.chave = chave 
        self.prox = None
    
class CircularEncadeada:
    def __init__(self):
        self.ptlista = No(None)
        self.ptlista.prox = self.ptlista

    def busca(self, valor):
        self.ptlista.chave = valor  
        ant = self.ptlista
        pont = self.ptlista.prox

        while pont.chave < valor:
            ant = pont
            pont = pont.prox
        
        return ant, pont
    
    def inserir(self, valor):
        self.ptlista.chave = valor
        ant, pont = self.busca(valor)

        novo_no = No(valor)

        novo_no.prox = pont
        ant.prox = novo_no
    
    def remover(self, valor):
        ant, pont = self.busca(valor)

        if pont != self.ptlista and pont.chave == valor:
            ant.prox = pont.prox
        else: 
            print("Valor nao encontrado")
```

```
no = No(10)
```

Esse "no" é um objeto que tem:
```
no.chave = 10  # pega o valor (“a chave do nó”)
no.prox = None # pega o próximo nó (o próximo nó)
```

```
A = No(10)
B = No(20)

A.prox = B    # significa isso
A.prox.chave  # signiifca que pegamos o valor de B , ou seja 20
```

Sobre o codigo
```
class No:
    def __init__(self, chave):
        self.chave = chave 
        self.prox = None
```

chave → valor
prox → próximo nó

```
def __init__(self):
        self.ptlista = No(None)
        self.ptlista.prox = self.ptlista
```
Lista circular vazia

self.ptlista → variável que guarda um nó
No(None) → cria o nó
self.ptlista.prox → acessa o “próximo”
self.ptlista.prox = self.ptlista → faz o nó apontar pra ele mesmo

Sobre a Busca
ex:
[ptlista] → 10 → 20 → 30 → (volta pro ptlista)

busca(20)

self.ptlista.chave = valor
ptlista.chave = 20 -> se torna isso
 
ant = self.ptlista -> ant = [ptlista]
pont = self.ptlista.prox -> pont = 10

while pont.chave < valor: -> 10 < 20 → True

ant = pont      # ant = 10
pont = pont.prox  # pont = 20

pont = 20

20 < 20 → False (Para o loop)

return ant, pont

ant = 10
pont = 20

O que retorna:
(ANTERIOR, POSIÇÃO ONDE DEVERIA ESTAR)

é se ele nao existir
[ptlista] → 10 → 20 → 30 → (volta)

busca(25)

self.ptlista.chave = 25

[ptlista(chave=25)]

ant = ptlista
pont = ptlista.prox

ant = ptlista
pont = 10

10 < 25 → True

ant = 10
pont = 20

20 < 25 → True

ant = 20
pont = 30

30 < 25 → False (Para o loop)

return ant, pont

ant = 20
pont = 30

O valor 25 não existe, mas:

20 < 25 < 30 -> Então a função te devolve exatamente onde ele deveria ser inserido

isso se conecta com inserção

```
novo_no.prox = pont
ant.prox = novo_no
```

novo_no.prox = 30
20.prox = novo_no

resultado final: 10 → 20 → 25 → 30 (A busca não serve só pra encontrar — ela serve pra posicionar)

Caso de inserção:
[ptlista] → 10 → 20 → 30 → (volta)

Busca(40):

Resultado: (isso foi feito graças a "ant, pont = self.busca(valor)" que pega toda a logica)
ant = 30
pont = ptlista (note que no ultimo ele volta e aponta para ptlista, ou seja, um ciclo)

Inserção:
novo_no = No(40)

novo_no.prox = pont   # 40 → ptlista
ant.prox = novo_no    # 30 → 40  (ant = 30 | ant.prox = 40)

resultado:
10 → 20 → 30 → 40 → (volta)

Busca decide ONDE, inserção faz o COMO

sobre a remoção
```
pont != self.ptlista # “não parei no sentinela” (se parou no ptlista → chegou no final → não encontrou)
```

```
pont.chave == valor # verifica se o valor realmente existe
```

ou seja, “o valor existe se: não é o sentinela e a chave é igual ao valor”

linha da remoção
```
ant.prox = pont.prox
```

10 → 20 → 30

ant = 10
pont = 20

ant.prox = pont.prox  -> 10.prox = 30

resultado: ele pula a 20 (O 20 foi removido da lista)
10 → 30

Remover = fazer o anterior apontar para o próximo

[ptlista] → 10 → 20 → 30 → (volta)

remover(20)

ant = 10
pont = 20

10 → 30


e se a valor estiver na primeira possição:
[ptlista] → 10 → 20 → 30 → (volta pro ptlista)

remover(10)

ant, pont = self.busca(10)

ant = ptlista
pont = 10

if pont != self.ptlista and pont.chave == valor:

pont != ptlista → True
pont.chave == 10 → True

ant.prox = pont.prox -> ptlista.prox = 20 (pont -> 10 | pont.prox -> 20)

resultado:
[ptlista] → 20 → 30 → (volta)

