# Localizando uma string dentro de outra
nome = str(input('Qual seu nome completo?')).strip()
print('Seu nome tem Silva?{}'.format('silva' in nome.lower()))
