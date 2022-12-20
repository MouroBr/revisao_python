# Calcula o custo de uma passagem de trem a partir da distância
distancia = float(input('Qual é a distância da sua viagem? '))

print(f'Total de quilometros será de: km{distancia}')
if distancia <= 200:
    preco = round(distancia * 0.5, 2)
else:
    preco = round(distancia * 0.45, 2)

print(f'O preço de sua passagem de trem é de R${preco}')