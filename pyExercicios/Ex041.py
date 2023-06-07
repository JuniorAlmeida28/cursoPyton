from datetime import date
nasci = int(input("Informe o ano de nascimento do atleta: "))
idade = date.today().year - nasci
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("O atleta está na categoria MIRIM!")
elif idade <= 14:
    print("O atleta está na categoria INFANTIL!") 
elif idade <= 19:
    print("O atleta está na categoria JUNIOR!")
elif idade <= 25:
    print("O atleta está na categoria SÊNIOR!") 
else:
    print("O atleta está na categoria MASTER!")              