
andares = 30

print("com o for: \n")

for i in range (1,andares):

    if(i == 13):
        continue

    print("andar "+ str(i))


print("com o while decrescente\n")


while(andares + 1 >= 1):

    

    if(andares != 13):
        print("andar "+ str(andares))

    andares = andares - 1


