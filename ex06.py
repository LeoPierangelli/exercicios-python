a = float(input('Digite a sua altura: '))
s = input('Digite 1(masculino) ou 2(feminino): ')
pi = (72.7*a) - 58
if s == 2:
    pi = (62.1*a) - 44.7

print(f'Seu peso ideal é {pi}')
