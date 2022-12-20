# Calculadoura de multas
velocidade = float(input('Qual a velocidade do veiculo? '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade de 80km')
    multa = round((velocidade - 80) * 7, 2)
    print(f'Voce foi multado em R${multa}')

else:
    print('Tenha uma boa viagem, dirija com segurança.')