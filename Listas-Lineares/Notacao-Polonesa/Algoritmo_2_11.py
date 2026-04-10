def infixa_para_polonesa(expresao):
    pilha = [] # sera nossa "sala de espera" para os operadores e decidir quem sai primeiro
    saida = [] # vamos ir colocando aqui ate forma a lista final (operação final)
    
    precedencia = { #dicionario para saber qual tem mais prioridade
        '+': 1, 
        '-': 1, 
        '*': 2, 
        '/': 2, 
        '^': 3
    }

    tokens = expresao.split() # vamos separa a expressao em pedaços


    for token in tokens:
        if token.isalnum(): # se for um operador vai direto para a saida
            saida.append(token)
        
        elif token == "(": # se for o "(" entra na pilha de espera
            pilha.append(token)
        
        elif token == ")": # se for o ")" resolvemos tudo que esta dentro dele
            while pilha and pilha[-1] != "(": # joga tudo pra saida ate achar "("
                saida.append(pilha.pop())
            pilha.pop() # removemos "(" da pilha, ele nao vai para a saida final
        
        else:
            #se ja tem um operador maior ou igual, ele deve sair da "sala de espera" e ir para saida antes do novo entrar
            while (pilha and pilha[-1] != "(" and 
                   precedencia.get(pilha[-1], 0) >= precedencia.get(token, 0)):
                saida.append(pilha.pop())
            
            pilha.append(token)
    
    while pilha: # a expressao acaba entao esvaziei qualquer exprecao que sobrou
        saida.append(pilha.pop())

    return " ".join(saida)


# TESTANDO O CÓDIGO

# Teste 1: Uma expressão simples
expr1 = "A + B"
print(f"Infixa:   {expr1}")
print(f"Polonesa: {infixa_para_polonesa(expr1)}\n")

# Teste 2: Expressão com precedência matemática
# O * tem que acontecer antes do +, mesmo vindo depois
expr2 = "A + B * C"
print(f"Infixa:   {expr2}")
print(f"Polonesa: {infixa_para_polonesa(expr2)}\n")

# Teste 3: Expressão com parênteses forçando prioridade
expr3 = "( A + B ) * C"
print(f"Infixa:   {expr3}")
print(f"Polonesa: {infixa_para_polonesa(expr3)}\n")
