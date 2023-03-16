#DESAFIO 3: Uma função que pede para o usuário um numero divisível por 2 e 3.
def mostraNumeroDivisivel():
    numero_valido = False
    
    while(numero_valido == False):
        try:
            numero = int(input("Digite um número divisível por 2 ou por 3 entre 0 e 100: "))
            if(numero >= 0 and numero <= 100 and numero % 2 == 0 or numero % 3 == 0):
                print("Parabéns, você escolheu um número válido: ", numero)
                numero_valido = True
            #elif(numero < 0 or numero > 100):
            #    print("O número está fora do intervalo de 0 à 100, digite novamente um número válido.")
            else:
                print("Você não digitou um número válido, favor se atentar a regra e digitar um número válido.")
        except:
            print("Tente novamente")

mostraNumeroDivisivel()