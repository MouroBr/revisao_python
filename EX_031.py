# Diz se o ano é bissexto ou não
from datetime import date
ano = int(input('Digite o ano que vc gostraria de saber se é Bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 == 0 or ano == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')
