# Calculadora de empréstimo
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de fianciamento:'))
prestacao = round(casa / (anos * 12), 2)
minimo = salario * 30 / 100

print(f'Valor da casa {casa} em {anos * 12}', end='')
print(f'A prestação será de R${prestacao}')

if prestacao <= minimo:
    print('\033[0;32mEmpréstimo CONCEDIDO\033[m')
else:
    print('\033[0;31mEmpréstimo NEGADO\033[m')

