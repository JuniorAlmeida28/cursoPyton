frase = "Curso em Video Python"
#Fatiamento
print(frase[9]) # Mostra apenas o caractere que estiver na posição 9
print(frase[9:13]) # Mostra do caractere 9 até o 12
print(frase[9:21:2]) # Mostra do carctere 9 ao 20 pulando de 2 em 2
print(frase[:5]) # Mostra do caractere 0 até a posição 5
print(frase[15:]) # Mostra do caractere 15 até o fim 
print(frase[9::3]) # mostra do caractere 9 pulando de 3 em 3 até o fim
print(frase[::2]) # Mostra do inicio até o fim pulando de 2 em 2

# Analise
print(len(frase)) # Mostra o comprimento dos caracteres
print(frase.count('o')) # Conta quantas letras especificas tem na frase
print(frase.count('o',0,13)) # conta quantas letras especificas do 0 até 12 existem
print(frase.find('deo')) # Diz quantas vezes encontrou 
print(frase.find('Android')) # Como não existe volta o valor -1
print('Curso' in frase) # Mostra se existe a palavra ou não (True or False)

# Transformação
print(frase.replace('Python', 'Android')) # Substitui a frase
print(frase.upper()) # Deixa tudo em maiusculo
print(frase.lower()) # Deixa tudo em minusculo
print(frase.capitalize()) # Deixa tudo em minusculo e só a primeira letra fica maiusculo
print(frase.title()) # Analisa quantas palavras existe na frase e deixa suas letras iniciais maiusculo
print(frase.strip()) # Remove todas as casas vazias do inicio e final
print(frase.rstrip()) # Remove todas as casas vazias do lado direito
print(frase.lstrip()) # Remove todas as casas vazias do lado esquerdo

# Divisão
print(frase.split()) # Tira os espaços e divide a frase colocanta em listas diferentes
print('-'.join(frase.split())) # Tira os espaços e divide a frase colocanta em listas diferentes e junta com o caractere que quiser
print()
