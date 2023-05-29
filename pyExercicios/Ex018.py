import math
num = float(input("Digite o valor do ângulo: "))
angulo_radianos = math.radians(num)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print("Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(seno, cosseno, tangente))
