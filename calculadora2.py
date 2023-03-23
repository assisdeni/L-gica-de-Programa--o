def calculadora():
    while True:
        print("Selecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        opcao = input("Opção escolhida: ")
        
        if opcao == '0':
            print("Encerrando a calculadora...")
            break
        elif opcao in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if opcao == '1':
                resultado = num1 + num2
                print(f"{num1} + {num2} = {resultado}")
            elif opcao == '2':
                resultado = num1 - num2
                print(f"{num1} - {num2} = {resultado}")
            elif opcao == '3':
                resultado = num1 * num2
                print(f"{num1} * {num2} = {resultado}")
            elif opcao == '4':
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
        else:
            print("Essa opção não existe")
            
        print()
        
calculadora()