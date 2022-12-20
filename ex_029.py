# Descobre se é par ou impar

num = int(input('Digite um número qualquer: '))
valor = num % 2
if valor == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é impar.')


