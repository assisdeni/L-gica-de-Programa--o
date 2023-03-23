nomes = ["Ricardo", "Joana", "Roberto", "Jadi", "Edvan", "Joana"]

def achar_nome(array,nome):
    nome_encontrado = False
    quantos_nomes = 0
    
    for i in range(len(array)):
        if array[i] == nome:
            nome_encontrado = True
            quantos_nomes = quantos_nomes + 1

    if nome_encontrado == True:
          print("O nome: ", nome, "foi encontrado ", quantos_nomes, "vezes!")
    else:
          print("Que pena, o ", nome, "não foi encontrado!")
        
achar_nome(nomes, "Joana")