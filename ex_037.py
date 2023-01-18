# Conversor Numérico
num = int(input(f'Diite um numero inteiro: '))
print('''Escolha a base para conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print(f'Em BINÁRIO {num} = {bin(num)}')
elif opcao == 2:
    print(f'Em OCTAL {num} = {oct(num)}')
elif opcao == 3:
    print(f'Em HEXADECIMAL {num} = {hex(num)}')
else:
    print('\033[0;31mOpção Invalida\033[m')



