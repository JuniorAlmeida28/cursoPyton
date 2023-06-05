a = float(input("Informe a reta A: "))
b = float(input("Informe a reta B: "))
c = float(input("Informe a reta C: "))
if a + b > c:
    if b + c > a:
        if c + a > b:
            print("As retas formam um triangulo!")
else:
    print("As retas não formam um triangulo!")            