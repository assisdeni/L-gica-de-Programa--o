# DESAFIO 2: Um função que pede para o usuário um numero par
def mostraNumeroPar():
    numero_valido = False

    while (numero_valido == False):
        try:
            numero = int(input("Digite um número par entre 0 e 100: "))

            if (numero >= 0 and numero <= 100 and numero % 2 == 0):
                print("Parabéns, você escolheu um número válido: ", numero)
                numero_valido = True
            else:
                print("Número inválido. Por favor, informe um número par entre 0 e 100")
        except:
            print("Você precisa digitar um número inteiro.")
mostraNumeroPar()