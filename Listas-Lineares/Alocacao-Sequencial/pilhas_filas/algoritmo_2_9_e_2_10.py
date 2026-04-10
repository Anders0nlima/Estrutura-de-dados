M = 5 # capacidade maxima    
F = [None] * M # memoeria fisica
f = -1 # frente 
r = -1 # ré

def inserir_fila(F, f, r, M, novo_valor):
    prov = (r + 1) % M # verifica se a fila nao esta vazia -> começa em 0

    if prov != f:
        r = prov
        F[r] = novo_valor

        if f == -1:
            f = 0

        print(f"Fila: {novo_valor} entrou na posição {r}.")
    else:
        print("Fila (Overflow): A fila está cheia!")
    return f, r

def remover_fila(F, f, r, M):
    if f != -1:
        valor_recuperado = F[f]
        F[f]  = None
        print(f"Fila : {valor_recuperado} foi removido.")

        if f == r:
            f = -1
            r = -1
        else:
            f = (f + 1) % M
        
    else:
        print("Fila (Underflow): Não há ninguém na fila!")
    
    return f, r

f, r = inserir_fila(F, f, r, M, 2)
f, r = inserir_fila(F, f, r, M, 6)
f, r = inserir_fila(F, f, r, M, 3)
f, r = inserir_fila(F, f, r, M, 9)
f, r = remover_fila(F, f, r, M)


# demostrações
print(f"Estado final da memória: {F}")
print(f"ponteiro f: {f}")
print(f"ponteiro r: {r}")


#O ponteiro r (ré) é quem trabalha aqui. A cada novo número, o r anda uma casa para a direita.
#Ele começou em -1, foi para 0 (valor 2), depois 1 (valor 6), depois 2 (valor 3) e parou no 3 (valor 9).
#Resultado parcial: O último a chegar (o 9) está na posição 3. Por isso o r é 3.


#O ponteiro f (frente) é quem manda na saída. No começo, o f estava em 0 (apontando para o 2).
#Quando você chamou remover_fila, o sistema "atendeu" quem estava na posição 0.
#O f então anda para a direita para apontar para a próxima pessoa da fila.
#Resultado final: O próximo a ser atendido agora é quem está na posição 1 (o valor 6). Por isso o f é 1.