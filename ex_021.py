# Teste de metodo de str
nome = str(input('Digite seu nome completo: ')).strip()

print('Todas as letras são maiusculas = {}'.format(nome.upper()))
print('Todas as letras são minusculas = {}'.format(nome.lower()))
print('Total de letras do primeiro nome = {}'.format(nome.find(' ')))
print('Total de letras = {}'.format(len(nome) - nome.count(' ')))



