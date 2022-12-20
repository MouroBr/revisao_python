# Jogo de adivinhação
from random import randint
from time import sleep

computador = randint(0, 5)  # seta um numero entre 0 e 5
print('-=-' * 20)
print('escolhendo numero...')
print('-=-' * 20)

jogador = int(input('Escolha um número entre 0 e 5: '))
print('Processando...')
sleep(3)
if computador == jogador:
    print('Eu escolhi {}'.format(computador))
    print('Você venceu!!! Parabéns...')
else:
    print('Eu escolhi {}'.format(computador))
    print('Você perdeu... huahauahauahauahau...')
