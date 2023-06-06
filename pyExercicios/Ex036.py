print("=" * 50)
print("Simulação de financiamento de casa")
print("=" * 50)
valorCasa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o salário do comprador: "))
anos = int(input("Informe em quantos anos será pago: "))

presta = valorCasa / (anos * 12)
porcentagem = salario * 0.30

if porcentagem >= presta:
    print("Seu emprestimo foi aprovado!!")
else:
    print("Emprestimo negado. As parcelas excedem 30% do seu salário!")    
    