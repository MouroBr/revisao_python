# Encontra o seno, cosseno e tangente de um angulo
import math
alpha = float(input('Digite o valor do angulo:'))

beta = math.radians(alpha)

hipotenusa =round(math.hypot(beta), 2)
seno = round(math.sin(beta), 2)
cosseno = round(math.cos(beta), 2)
tangente = round(math.tan(beta), 2)

print(f'Seno = {seno}\nCosseno = {cosseno}\nTangente = {tangente}')