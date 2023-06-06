a = float(input("Informe a reta A: "))
b = float(input("Informe a reta B: "))
c = float(input("Informe a reta C: "))
if a + b > c:
    if b + c > a:
        if c + a > b:
            if a == b and b == c:
                print("As retas formam um triangulo Equilátero: todos os lados iguais")
            elif a == b != c or a == c != b or b == c != a:
                print("As retas formam um triangulo Isósceles: dois lados iguais") 
            else:
                print("As retas formam um triangulo Escaleno: todos os lados diferntes")       
else:
    print("As retas não formam um triangulo!")  