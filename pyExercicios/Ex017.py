import math
cateto_oposto = float(input("Digite o cumprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o cumprimento do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print("O cumprimento da Hipotenusa é: {:.2f}".format(hipotenusa))