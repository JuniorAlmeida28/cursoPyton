num = int(input("Informe um número: "))
base = int(input("Escolha a base de conversão. (1 - Binário, 2 - Octal, 3 - Hexadecimal): "))

if base == 1:
    result = bin(num)
    print("O número {} em Binário é: {}".format(num, result))
elif base == 2:
    result = oct(num)
    print("O número {} em Octal é: {}".format(num, result))
elif base == 3:
    result = hex(num)
    print("O número {} em Hexadecimal é: {}".format(num, result))
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")    