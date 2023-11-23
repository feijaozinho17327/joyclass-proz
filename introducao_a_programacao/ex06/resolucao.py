
while True:
 
 try:
  
  nome = str(input("digite seu nome "))
  ano = int(input("digite seu ano de nascimento "))
 except ValueError:
  print("dado invalido")
  continue
 if ano > 2021 or ano < 1922:
  print("ano incompativel")
 else:
  idade = 2022 - ano
  print(nome + " sua idade e " + str(idade))
  break
