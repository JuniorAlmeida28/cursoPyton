import random
num = int(input("Adivinhe um número de 0 a 5: "))
num2 = random.randint(0, 5)
if num == num2:
    print("Você acertou o computador escolheu o número {}!".format(num2))
    print("Parabéns!!!!")
else:
    print("Você errou o computador escolheu o número {}".format(num2)) 
       