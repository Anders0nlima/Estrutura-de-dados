# Resumo: Listas Lineares em Alocação Sequencial

Este documento descreve as operações fundamentais em listas onde a
memória é alocada de forma contígua (vetores/arrays), utilizando uma
variável $n$ para controlar o número de elementos válidos e $M$ para a
capacidade máxima.

------------------------------------------------------------------------

## 1. Algoritmos de Busca

### 1.1. Busca Sequencial (Simples)

-   **Conceito:** Percorre a lista do início ao fim comparando cada
    elemento com a chave $x$.
-   **Lógica:** Possui dois testes por iteração: se o índice ainda é
    válido ($i \le n$) e se o elemento foi encontrado.
-   **Complexidade:** $O(n)$.

### 1.2. Busca com Sentinela

-   **Conceito:** Uma otimização da busca sequencial. Insere-se a chave
    $x$ na posição $n+1$.
-   **Diferencial:** Elimina o teste de limite do índice ($i \le n$)
    dentro do laço, pois o algoritmo certamente encontrará $x$ (mesmo
    que seja no final).
-   **Complexidade:** $O(n)$, porém com menos operações lógicas por
    iteração.

### 1.3. Busca em Lista Ordenada (Sequencial)

-   **Premissa:** A lista deve estar em ordem (ex: crescente).
-   **Conceito:** Realiza a busca linear, mas pode parar antecipadamente
    se encontrar um número maior que $x$.
-   **Diferencial:** Melhora o tempo de resposta para buscas sem
    sucesso.
-   **Complexidade:** $O(n)$.

### 1.4. Busca Binária

-   **Premissa:** Exige obrigatoriamente que a lista esteja ordenada.
-   **Conceito:** Estratégia de "dividir para conquistar". Compara $x$
    com o elemento central. Se não for igual, descarta metade da lista e
    repete o processo.
-   **Complexidade:** $O(\log n)$. É o algoritmo de busca mais eficiente
    para grandes volumes de dados.

------------------------------------------------------------------------

## 2. Algoritmos de Manipulação

### 2.1. Inserção

**Procedimento:** 
1. **Verificação de Overflow:** Garante que $n < M$ (há espaço na memória). 
2. **Unicidade:** Realiza uma busca para garantir que o elemento não é duplicado. 
3. **Ação:** Adiciona o elemento na posição $n+1$ e incrementa $n$.


### 2.2. Remoção

**Procedimento:** 
1. **Verificação de Underflow:** Garante que a lista não está vazia ($n \neq 0$). 
2. **Busca:** Localiza o índice do elemento a ser removido. 
3. **Deslocamento (Shifting):** Move todos os elementos à direita do índice removido uma posição para a esquerda para não deixar "buracos". 
4. **Ação:** Decrementa o valor de $n$.

