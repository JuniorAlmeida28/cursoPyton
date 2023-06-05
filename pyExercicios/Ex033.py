num1 = int(input("Informe o número 1: "))
num2 = int(input("Informe o número 2: "))
num3 = int(input("Informe o número 3: "))

if num1 <= num2:
    if num1 <= num3:
        if num2 <= num3:
            print("O menor é: {} e o maior é: {}".format(num1, num3)) 
        else:    
            print("O menor é: {} e o maior é: {}".format(num1, num2)) 
    if num1 >= num3:
        if num2 >= num3:
            print("O menor é: {} e o maior é: {}".format(num3, num2)) 
        else:  
            print("O menor é: {} e o maior é: {}".format(num2, num3))          
if num1 >= num2:
    if num1 >= num3:
        if num2 >= num3:
            print("O menor é: {} e o maior é: {}".format(num3, num1))
        else:
            print("O menor é: {} e o maior é: {}".format(num2, num1))   
    if num1 <= num3:
        if num2 <= num3:
            print("O menor é: {} e o maior é: {}".format(num2, num3))         
            