a = float(input('Digite o valor de um ângulo: '))
b = float(input('Digite o valor de outro ângulo: '))
c = float(input('Digite o valor do último ângulo: '))

if a == 90 or b == 90 or c == 90:
    print('triângulo retângulo')
elif a>90 or b>90 or c>90:
    print('triângulo obtuso')
else:
    print('triângulo acutângulo')
