def mostrarNumero():
    numero_valido = False
    
    while(numero_valido == False):
        try:
            numero = int(input("Digite um número de 0 à 100: "))
            
            if(numero >= 0 and numero <= 100):
                print("Parabéns, você escolheu um número válido: ", numero)
                numero_valido = True
            else:
                print("Por favor, escolha um número válido de 0 a 100.")
        except:
            print("Você precisa digitar um número inteiro.")    
mostrarNumero()            