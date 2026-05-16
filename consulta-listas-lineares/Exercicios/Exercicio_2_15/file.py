"""
2.15 Imprimir, a partir de uma expressão em notação polonesa, a sequência de operações a serem executadas na ordem correta. Introduzir operandos especiais para armazenar resultados parciais.
NOTAÇÃO POLONESA (PÓS-FIXA) 
"""
def imprimir_operacoes(expressao):
    pilha = []
    temp_count = 1

    print("Sequência de operações:")

    for simbolo in expressao:
        if simbolo.isalnum():
            pilha.append(simbolo)
        else:
            op2 = pilha.pop()
            op1 = pilha.pop()
            temp = f"T{temp_count}"
            temp_count += 1
            print(f"{temp} = {op1} {simbolo} {op2}")
            pilha.append(temp)

    print("Resultado final:", pilha[-1])


expressao = "AB+C*"

print("Expressão (pós-fixa):", expressao)
print()
imprimir_operacoes(expressao)