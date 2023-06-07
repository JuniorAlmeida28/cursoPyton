sumIdade = 0
maior = 0
nome2 = ""
sumFemi = 0
for i in range(4):
    nome = str(input("Informe seu nome: "))
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Informe o seu sexo: ")).upper()
    sumIdade += idade
    if sexo in "Mm":
        if maior < idade:
            maior = idade
            nome2 = nome
    if sexo in "Ff":
        if idade < 20:
            sumFemi += 1
media = sumIdade / 4
print("A média de idade é: {:.2f}".format(media))
print("O homem mais velhor é: {}".format(nome2))
print("Existem {} mulheres com menos de 20 anos.".format(sumFemi))                    
        
    