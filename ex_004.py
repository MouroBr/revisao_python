# Dissecando uma variável.
a = input('Digite algo:')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiusculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
