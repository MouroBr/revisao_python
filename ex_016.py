# Mostrando a porção inteira de um numero racional usando bibliotecas
from math import trunc
numero = float(input('Digite um numero do tipo float:'))

inteiro = trunc(numero)

print('O numero digitado é {} e seu valor inteiro é {}'.format(numero, inteiro))
