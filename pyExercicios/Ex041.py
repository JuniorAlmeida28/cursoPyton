from datetime import date
nasci = int(input("Informe o ano de nascimento do atleta: "))
idade = date.today().year - nasci
print(idade)
if idade <= 9:
    print("O atleta está na categoria MIRIM!")
elif idade >= 10 and idade <= 14:
    print("O atleta está na categoria INFANTIL!") 
elif idade >= 15 and idade <= 19:
    print("O atleta está na categoria JUNIOR!")
elif idade == 20:
    print("O atleta está na categoria SÊNIOR!") 
else:
    print("O atleta está na categoria MASTER!")              