def Calc_idade(nome_completo, ano_nascimento, ano_atual):
    idade = False

    while (idade == False):   
        try:        
            if (ano_nascimento >= 1922 or ano_nascimento <= 2021):
                idade = ano_atual - ano_nascimento
                print ("A idade do(a) ", nome_completo, " é: ", idade, "!")
                idade = True
            else:
                print("Ano de nascimento inválido. Tente novamente.")
        except:
            print("Ocorreu um erro. Digite uma data válida.")
                
nome_completo = input("Digite o seu nome completo: ")
ano_nascimento = int(input("Digite o seu ano de nascimento (entre 1922 e 2021): "))
ano_atual = 2022

Calc_idade()
    
    


