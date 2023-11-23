def calcular(aux, num1, num2):
 
 if aux == 1:
  return num1 + num2
 
 if aux == 2:
  return num1 - num2
 
 if aux == 3:
  return num1 * num2
 
 if aux == 4:
  if num1 == 0 or num2 == 0:
   return "impossivel dividir por zero"
  else:
   return num1 / num2
  
  
while True:
 print("1: Soma \n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair")
 print("\ndigite o que deseja")
 aux = int(input())  
 
 if aux == 0:
  break

 print("digite o primeiro numero")
 num1 = int(input())  

 print("digite o segundo numero")
 num2 = int(input())  

 print("o resultado é "+ str(calcular(aux,num1,num2)))

  
