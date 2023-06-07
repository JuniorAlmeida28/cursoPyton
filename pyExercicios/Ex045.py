import random
print("{:=^50}".format(" JOKENPÔ "))
print("""Informe a sua escolha 
[ 1 ]- Pedra
[ 2 ]- Papel
[ 3 ]- Tesoura""")
user = int(input("Opção: "))
pc = random.randint(1,3)

if user == pc:
    print("Empate!!!")
elif user != pc:
    if user == 1 and pc == 3:
        print("Você escolheu Pedra e o Computador Tesoura")
        print("Parabéns, você venceu!!!")
    elif user == 3 and pc == 2:
        print("Você escolheu Tesoura e o Computador Papel")
        print("Parabéns, você venceu!!!")
    elif user == 2 and pc == 1:
        print("Você escolheu Papel e o Computador Pedra")
        print("Parabéns, você venceu!!!")
    elif user == 3 and pc == 1:
        print("Você escolheu Tesoura e o Computador Pedra")
        print("O computador venceu!!!")
    elif user == 2 and pc == 3: 
        print("Você escolheu Papel e o Computador Tesoura")                   
        print("O computador venceu!!!")
    elif user == 1 and pc == 2:
        print("Você escolheu Pedra e o Computador Papel")
        print("O computador venceu!!!")
    else:
        print("Valor informado é invalido. Tente novamente!!")            