numero = int(input("Digite um número inteiro: "))

# Um número primo é maior que 1
if numero > 1:
    # Verifica se o número é divisível por algum número menor que ele
    for i in range(2, numero):
        if (numero % i) == 0:
            print("O número não é primo.")
            break
    else:
        print("O número é primo.")
else:
    print("O número não é primo.")
