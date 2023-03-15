quantidadeRodas = int(input("Quantas rodas o veículo possui? "))
quantidadePessoas = int(input("Quantos passageiros o veículo irá transportar? "))
peso = float(input("Qual é o peso do veículo? "))

if (quantidadeRodas >= 2 ) and (quantidadeRodas <= 3):
    print ("A categoria indicada é a A")
elif (quantidadeRodas == 4) and (quantidadePessoas <= 8) and ( peso < 3.500):
    print ("A categoria indicada é a B!")
elif (quantidadeRodas >= 4) and (peso >= 3.500 and peso <= 6.000):
    print ("A categoria indicada é a C!")
elif (quantidadeRodas >= 4) and (quantidadePessoas > 8):
    print ("A categoria indicada é a D!")
elif (quantidadeRodas >= 4) and (peso > 6000):
    print ("A categoria indicada é a E!")