rodas = int(input("digite a quandidade de rodas: "))
peso = float(input("digite o peso do veiculo: "))
pessoas = int(input("digite quantas pessoas o veiculo comporta: "))


if (rodas <=3):
    print("cnh categoria A")
elif(rodas == 4 and pessoas <=8 and peso <=3500):
    print("cnh categoria B")
elif(rodas >= 4 and peso >= 3500 and peso <= 6000):
    print("cnh categoria C")
elif(rodas >= 4 and peso >= 6000):
    print("cnh categoria D")
else:
    print("veiculo não catalogado")
