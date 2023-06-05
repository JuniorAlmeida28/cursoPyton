salario = float(input("Informe o seu salário: "))
if salario > 1250.00:
    aumento = salario + (salario * 0.10)
    print("O seu salário de R${:.2f}, teve um aumento de 10% e ficou R${:.2f}".format(salario, aumento))
else:
    aumento = salario + (salario * 0.15)
    print("O seu salário de R${:.2f}, teve um aumento de 15% e ficou R${:.2f}".format(salario, aumento))  