n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1 + n2) / 2

if media < 5.0:
    print("O aluno está reprovador!!!")
elif media == 5.0 and 6.9:  
    print("O aluno está de recuperação!!!")
else:
    print("O aluno está aprovado!!!")      