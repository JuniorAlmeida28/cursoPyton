distancia = int(input("Informe a distancia em km: "))
if distancia <= 200:
    print("O valor da passagem é R${:.2f}".format(distancia * 0.50))
else:
    print("O valor da passagem é R${:.2f}".format(distancia * 0.45))    