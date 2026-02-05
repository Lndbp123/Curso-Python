num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operacao = input("Digite a operacao (+, -, *, /): ")

resultado = None
while resultado is None:
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisao por zero nao e permitida")
            operacao = input("Digite a operacao (+, -, *, /): ")
    else:
        print("Operacao invalida. Tente novamente.")
        operacao = input("Digite a operacao (+, -, *, /): ")
print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")