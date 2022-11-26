# Conversor de Reais para Dólar:
carteira = float(input('Digite o valor a ser convertido:R$'))
cotacaoDolar = float(input("Digite a cotação atual do Dólar:US$"))

valorFinal = round((carteira / cotacaoDolar), 2)

print(f'Você possui US${valorFinal}')
