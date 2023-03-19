#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
#Laço de repetição For em ordem decrescente

for i in range (20,0,-1):
    if(i == 13):
        continue
    print("Este é o", i,"° andar" )