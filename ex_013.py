# Calculadora de reajuste salarial
x = float(input('Digite o preço do produto:R$'))
y = float(input('Digite o valor do desconto:%'))

porcentagem = round(x * (y / 100), 2)
reajuste = x + porcentagem

print(f'O salário reajustado é de R${reajuste}')
