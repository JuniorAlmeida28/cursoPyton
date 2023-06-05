Velocidade = float(input("Informe a velocidade: "))
if Velocidade > 80:
    print("Você recebeu uma multa!")
    multa = (Velocidade - 80) * 7.00
    print("O valor da sua multa é: R${:.2f}".format(multa))
else:
    print("Você não foi multado! Parabéns!!!!")    