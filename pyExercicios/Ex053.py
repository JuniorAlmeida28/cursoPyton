frase = input("Digite uma frase: ")
frase = frase.replace(" ", "")  # Remove os espaços da frase

# Verifica se a frase invertida é igual à frase original
if frase == frase[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
