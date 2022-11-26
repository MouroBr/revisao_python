# Calculadora de descontos
x = float(input('Digite o preço do produto:R$'))
y = float(input('Digite o valor do desconto:%'))

porcentagem = round(x * (y / 100), 2)
desconto = x - porcentagem

print(f'O preço com o desconto é R${desconto}')
