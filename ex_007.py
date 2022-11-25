# Calcula a média aritmética entre as notas de um aluno.
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

media = float(nota1 + nota2) / 2
round(media, 2)

print(f'A média entre {nota1} e {nota2} é igual a {media}')

