peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))
imc = peso / (altura ** 2)

print("O seu IMC É: {:.2F}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso!!")
elif imc >= 18.5 and imc < 25:
    print("Você está no seu peso ideal!!") 
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso!!")
elif imc >= 30 and imc < 40:
    print("Você está com obesidade!!")
else:
    print("Você está com obsidade mórbida!!")               