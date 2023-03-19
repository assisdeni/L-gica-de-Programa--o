def calcular ():
    n1 = int(input("Digite o primeiro número da operação: "))
    n2 = int(input("Digite o segundo número da operação: "))
    op = input("Qual operação deseja realizar? Digite multiplicação, divisão, soma ou subtração? ")
    resultado = 0
    
    if ( op == "multiplicação"):
        resultado = n1 * n2
        return(resultado)
    elif (op == "divisão"):
        resultado = n1 / n2
        return(resultado)
    elif (op == "soma"):
        resultado = n1 + n2
        return(resultado)
    elif (op == "subtração"):
        resultado = n1 - n2
        return(resultado)
    elif (op != "multiplicação" or op != "divisão" or op != "soma" or op != "subtração"):
        resultado = 0
        return(resultado)

res = calcular()
print(res)