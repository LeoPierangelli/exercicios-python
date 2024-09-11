v = int(input('Digite a velocidade em km/h: '))

if v < 80:
    print('não há multa')
else:
    if v >= 80 and v <= 100:
        multa = v*1.2
    elif v > 100 and v <= 120:
        multa = 100*1.2 + v*1.3
    elif v > 120:
        multa = 100*1.2 + 120*1.3 + v*1.4

    print(f'valor da multa: R${multa:.2f}')
