# Calcula o valor do aluguel de um veiculo
quilometros_percorridos = float(input('Digite o total de Quilometros percorridos: Km'))
diaria = float(input('Digite o valor da diária: '))

total_quilometros = (quilometros_percorridos * 0.15)
total_diario = (diaria * 60)
valor_total = round(float((total_quilometros) + (total_diario)), 2)
print()
print(f'Total Quilômetro rodado =R${total_quilometros}\nTotal diárias =R${total_diario}\nTotal =R${valor_total}')
