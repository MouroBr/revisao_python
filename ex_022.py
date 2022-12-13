# Separa um digito em unidade, dezena, centena e milhar.
numero = str(input('Informe um numero entre 0 e 9999: '))
separador = numero.split()
print(f'Unidade = {separador[0][3]}')
print(f'Dezena  = {separador[0][2]}')
print(f'Centena = {separador[0][1]}')
print(f'Milhar  = {separador[0][0]}')