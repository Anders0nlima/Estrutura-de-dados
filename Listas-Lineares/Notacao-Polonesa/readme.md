# Sobre a pasta: O exemplo da notação polonesa é uma aplicação real de pilha

problema: O problema da notação infixa para os computadores é que ela exige regras chatas de precedência (multiplicação antes de adição) e o uso de parênteses para quebrar essas regras: $(A + B) \times C$. O computador teria que ler a expressão inteira, ir e voltar várias vezes para descobrir o que calcular primeiro.

Para resolver isso, os matemáticos criaram a Notação Polonesa Reversa (também chamada de Pós-fixada). Nela, o operador vem depois dos números.

### Infixa: $A + B$
### Pós-fixada (Polonesa Reversa): $A \ B \ +$
### Infixa com parênteses: $(A + B) \times C$
### Pós-fixada: $A \ B \ + \ C \ \times$

A grande vantagem: Na Notação Polonesa, não existem parênteses e não existem regras de prioridade complexas. O computador só precisa ler da esquerda para a direita uma única vez, e quando ele acha um operador, ele aplica imediatamente nos dois últimos números que viu. É por isso que calculadoras e compiladores amam essa notação.

## Por que precisamos de uma Pilha para fazer essa conversão?

Imagine que você está lendo a expressão $A + B \times C$ da esquerda para a direita.

### Você lê o $A$. (Fácil, pode ir para a saída).
### Você lê o $+$. (Opa, não posso aplicar ele ainda, preciso ver o que vem depois).
### Você lê o $B$. (Vai para a saída).
### Você lê o $\times$.

Neste momento, você tem um $+$ e um $\times$ aguardando. Quem deve ser resolvido primeiro? A multiplicação! Portanto, o último operador que você encontrou ($\times$) é o primeiro que deve ir para a saída.Essa lógica de "o último a entrar é o primeiro a sair" é exatamente a definição de uma Pilha (LIFO).A pilha funciona como uma "sala de espera" para os operadores e parênteses. Eles ficam lá guardados até chegar o momento certo de irem para a expressão final.