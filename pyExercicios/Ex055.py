maior = 0
for i in range(5):
    peso = float(input("Informe o seu peso: "))
    menor = peso
    if menor > maior:
        maior = menor
print("""O maior é: {}
O menor é: {}""".format(maior, menor))        
    