# =========================
# 2.15 - NOTAÇÃO POLONESA (PÓS-FIXA)
# =========================

def imprimir_operacoes(expressao):
    pilha = []
    temp_count = 1

    print("Sequência de operações:\n")

    for simbolo in expressao:
        # Se for operando (letra ou número)
        if simbolo.isalnum():
            pilha.append(simbolo)

        # Se for operador
        else:
            op2 = pilha.pop()
            op1 = pilha.pop()

            temp = f"T{temp_count}"
            temp_count += 1

            print(f"{temp} = {op1} {simbolo} {op2}")

            pilha.append(temp)

    print("\nResultado final:", pilha[-1])


# =========================
# TESTE
# =========================

expressao = "AB+C*"

print("Expressão (pós-fixa):", expressao)
print()

imprimir_operacoes(expressao)