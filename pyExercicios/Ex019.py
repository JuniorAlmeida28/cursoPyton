import random
aluno1 = input('Digite o nome do aluno1: ')
aluno2 = input('Digite o nome do aluno2: ')
aluno3 = input('Digite o nome do aluno3: ')
aluno4 = input('Digite o nome do aluno4: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)
print("Aluno sorteado: {}".format(sorteado))