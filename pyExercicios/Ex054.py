menor = 0
maior = 0
for i in range(1,8):
    idade = int(input("Informe a sua idade: "))
    if idade < 18:
        menor += 1
    else:
        maior += 1
print("""{} Pessoa atingiram a maioridade.
{} Pessoa não atingiram a maioridade.""".format(maior, menor))            
    