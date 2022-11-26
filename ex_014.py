# Conversor de temperatura (C° para F°)
celcios = float(input('Digite a temperatura a ser convertida:C°'))

fahrenheit = round(float((celcios * 1.8) + 32), 2)

print(f'{celcios}°C é equivvalente a {fahrenheit}°F.')
