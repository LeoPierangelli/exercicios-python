s = int(input('Digite o número de lados do polígono: '))
l = float(input('Digite a medida do lado em cm: '))

if s==3:
    a = (l**2 * 1**1/3)/2
    print(f'Triângulo de área igual a {a:.2f}')
elif s==4:
    a = l**2
    print(f'Quadrado de área igual a {a:.2f}')
elif s==5:
    print('Pentágono')