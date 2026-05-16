"""
Comparar o algoritmo apresentado com o Algoritmo 2.3:
função busca-ord1(x) 
           se x ≤ L[n] . chave então 
                     i := 1 
                     enquanto L[i] . chave < x faça 
                               i := i + 1 
                     se L[i] . chave ≠ x então 
                               busca-ord1 := 0 % elemento não encontrado 
                     senão busca-ord1 := i % elemento encontrado 
           senão busca-ord1 := 0 % fora da tabela 
           
algoritmo 2.3:
função busca-ord(x) 
       L[n + 1] . chave := x;   i := 1 
       enquanto L[i] . chave < x faça 
             i := i + 1 
       se i = n + 1 ou L[i] . chave ≠ x então 
                busca-ord := 0 
       senão busca-ord := i

Em que situação o desempenho dos dois é equivalente? 
o sentido de equivalencia está na quantidade de interações, eles se tornam equivalentes no pior caso de ambos. Eles são equivalentes na quantidade de memória acessada (os n elementos) quando a busca é forçada a ir até o final da lista.
em casos normais como o algoritmo 2.3 possui um sentinela (faz apenas uma comparação por iteração) e o algortimo 2.4 faz duas, o 2.3 acaba ganhando em eficiencia
Qual é a restrição que o algoritmo acima apresenta em relação ao Algoritmo 2.3? 
definição de restrição: O que os meus dados precisam ter para que esse algoritmo funcione?
A restrição do algoritmo 2.4 é que a lista precisa estar ordenada.
O Algoritmo 2.3 (Busca Sequencial comum) funciona em qualquer lista, bagunçada ou não. Se usar o algoritmo da 2.4 em uma lista desordenada, ele pode parar no segundo elemento (se ele for maior que x) e dizer que não encontrou, mesmo que o x esteja logo depois.
"""