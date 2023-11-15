def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Não é possível dividir por zero."

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = int(input("Digite: \n1 - soma \n2 - subtração \n3 - multiplicação \n4 - divisão\n"))

if operacao == 1:
    print(soma(num1, num2))
elif operacao == 2:
    print(sub(num1, num2))
elif operacao == 3:
    print(mult(num1, num2))
elif operacao == 4:
    print(div(num1, num2))
else:
    print("Opção inválida")


