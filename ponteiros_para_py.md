### Onde está o “ponteiro” no código?

- prox é um “ponteiro” para outro nó
```
self.prox = None

# exemplo

a = No(10)
b = No(20)

a.prox = b

```

- isso signifca que a.prox está guardando a referência de b (a → b)
- Em Python, variáveis são referências (ponteiros invisíveis) para objetos.