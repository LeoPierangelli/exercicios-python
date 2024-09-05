a = float(input('Digite a sua altura: '))
s = input('Digite o seu sexo: ')

if s == 'Masculino':
    pi = (72.7*a) - 58
else:
    pi = (62.1*a) - 44.7

print(f'Seu peso ideal é {pi}')
