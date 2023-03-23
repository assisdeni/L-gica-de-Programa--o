cesta = ["Maçã", "Banana", "Laranja", "Uva", "Abacaxi", "Manga","Abacaxi","Uva"]

def achar_fruta(array):
    fruta_encontrada = False
    quantas_frutas = 0
    fruta_escolhida = False

    while fruta_escolhida == False:
        nome_fruta = input("Informe uma fruta que você deseja: ")
        
        for i in range(len(array)):
            if array[i] == nome_fruta:
                fruta_encontrada = True
                fruta_escolhida = True
                quantas_frutas = quantas_frutas + 1

    if fruta_encontrada == True:
      print("Você escolheu a fruta: ",nome_fruta)
    else:
      print("A fruta ", nome_fruta, "escolhida não foi encontrada!")
      
achar_fruta(cesta)

