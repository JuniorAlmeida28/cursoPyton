idade = int(input("Informe a sua idade: "))

if idade > 18:
    passou = idade - 18
    print("Você passou {} anos do tempo de alistamento!".format(passou))
elif idade < 18:
    falta = 18 - idade
    print("Você vai se alistar em {} anos!".format(falta))
else:
    print("É hora de fazer o seu alistamento!")        