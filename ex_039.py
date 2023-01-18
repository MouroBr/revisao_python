def dataAlistamento (anoNascimento):
    alistamento = 2023
    tempoParaAlistamento = alistamento - anoNascimento

    if tempoParaAlistamento < 18:
        print('O Sr. vai se alistar em {} anos'.format( tempoParaAlistamento))

    elif tempoParaAlistamento == 18:
        print('O Sr se alista exatamente nesse ano')

    else:
        print('O SR. já deveria ter se alistado')


dataAlistamento(2015)
