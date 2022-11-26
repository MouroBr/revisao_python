# Calcula a quantidade de tinta para pintar uma parede
largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede: '))
tinta = float(input('Digite o rendimento da tinta: m^2/l'))

area_parede = round(float(largura * altura), 2)
rendimento = round(float(area_parede / tinta))

print(f'A área {area_parede} a quantidade de tinta necessária para pinta a parede é {rendimento}')