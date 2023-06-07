primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos da PA são:")

for c in range(10):
    termo = primeiroTermo + (c * razao)
    print(termo)
