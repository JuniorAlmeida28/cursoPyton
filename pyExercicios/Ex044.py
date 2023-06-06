valor = float(input("Informe o valor a ser pago: "))
tipoPag = int(input("Informe a forma de pagamento (1- À vista Dinheiro ou Cheque, 2- À vista Cartão, 3- Em 2x no Cartão, 4- Em 3x ou mais no Cartão): "))

if tipoPag == 1:
    total = valor - (valor * 0.10)
    print("O total a pagar é de R${:.2f}".format(total))
elif tipoPag == 2:
    total = valor - (valor * 0.05)
    print("O total a pagar é de R${:.2f}".format(total))
elif tipoPag == 3:
    total = valor / 2
    print("O total a pagar é 2X de R${:.2f}".format(total)) 
elif tipoPag == 4:
    total = valor + (valor * 0.20)
    print("O total a pagar é de R${:.2f}".format(total))       
else:
    print("Tipo de pagamento invalido. Tente novamente!")        