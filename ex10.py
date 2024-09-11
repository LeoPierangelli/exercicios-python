a = float(input('Digite a medida de um lado: '))
b = float(input('Digite a medida do outro lado: '))
c = float(input('Digite a medida do último lado: '))

if a == b and a == c:
    triangulo = 'equilátero'
elif a != b and b != c and a != c:
    triangulo = 'escaleno'
else:
    triangulo = 'isósceles'

print(f'Triângulo {triangulo}')

