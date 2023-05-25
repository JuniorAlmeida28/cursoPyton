preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O novo preço com desconto de 5% é: R${:.2f}'.format(novo))