a = float(input('Digite o valor de um ângulo: '))
b = float(input('Digite o valor de outro ângulo: '))
c = float(input('Digite o valor do último ângulo: '))

if a == 90 or b == 90 or c == 90:
    triangulo = 'retângulo'
elif a > 90 or b > 90 or c > 90:
    triangulo = 'obtuso'
else:
    triangulo = 'acutângulo'
print(f'Triângulo {triangulo}')

