num = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == "+":
    print(num + num2)
elif operacao == "-":
    print(num - num2)
elif operacao == "/":
    print(num / num2)
elif operacao == "*":
    print(num * num2)
else:
    print("Operação inválida!")
