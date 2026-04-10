# O Conceito
Imagine que você tem uma lista de números desordenados. A ordenação por distribuição funciona assim:
# Análise por Dígito: 
O algoritmo olha para o dígito menos significativo (a unidade), depois para a dezena, centena, e assim por diante.
# Distribuição em Filas ($F_k$): 
Para cada dígito (na base 10, de 0 a 9), existe uma fila correspondente ($F_0, F_1, ..., F_9$). O número é inserido na fila que corresponde ao seu dígito atual.
# Por que filas? 
Porque as filas garantem a estabilidade. O primeiro número a entrar em uma fila com o dígito "5" deve ser o primeiro a sair, mantendo a ordem relativa que ele já conquistou nos passos anteriores.
# Coleta e Repetição: 
Após distribuir todos os números, você os coleta das filas (da $F_0$ até a $F_9$) e reconstrói a lista. Esse processo se repete para o próximo dígito à esquerda até que o número com mais dígitos tenha sido processado.


### Explicação do Algoritmo 2.22
- Para $i = 1, ..., d$: Este loop controla as "passadas". Se o maior número tiver 3 dígitos, o loop roda 3 vezes.

- $k := i$-ésimo dígito menos significativo: Extrai o dígito atual para decidir em qual fila o número entra.

- $F_k \Leftarrow L[j]$: O número da lista original é inserido na fila $F_k$ (operação de inserção na fila, similar ao Algoritmo 2.20).

- Enquanto $F_k \neq \emptyset$ faça $L[j] \Leftarrow F_k$: Os números são removidos das filas e colocados de volta na lista $L$ (operação de remoção da fila, similar ao Algoritmo 2.21).