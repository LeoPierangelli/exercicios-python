a = float(input('Digite a medida de um lado: '))
b = float(input('Digite a medida do outro lado: '))
c = float(input('Digite a medida do último lado: '))

if a == b == c:
    print('Triângulo Equilátero')
elif a != b and b != c and a != c:
    print('Triângulo Escaleno')
else:
    print('Triângulo Isósceles')

