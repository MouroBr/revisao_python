# Calculadora para hipotenusa.
import math
catoposto = float(input('Digite o valor do cateto oposto: '))
catadjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.sqrt(((catadjacente) ** 2) + ((catoposto) ** 2))

round(hipotenusa, 2)
print(f'A hipotenusa = {hipotenusa}')
