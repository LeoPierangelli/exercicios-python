'''s = int(input('Digite o número de lados do polígono: '))
l = float(input('Digite a medida do lado em cm: '))

if s<3:
    print('Não é um polígono.')
elif s==3:
    a = (l**2 * 1**1/3)/2
    print(f'Triângulo de área igual a {a:.2f}')
elif s==4:
    a = l**2
    print(f'Quadrado de área igual a {a:.2f}')
elif s==5:
    print('Pentágono')
else:
    print('Polígono não identificado')'''


lados = int(input('diga a qtd de lados: '))
if lados < 3:
    print('não é um polígono')
elif lados > 5:
    print('polígono não identificado')

else:
    comprimento = float(input('Diga o tamanho do lado: '))

    perimetro = lados*comprimento
    if lados == 3:
        poligono = 'Triângulo'
    elif lados == 4:
        poligono = 'Quadrado'
    else:
        poligono = 'Pentágono'

    print(f'{poligono} de perímetro {perimetro}')
