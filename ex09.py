a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite o último valor: '))

if a > b and a > c:
    print(f'{a}')
elif b > c and b > a:
    print(f'{b}')
else:
    print(f'{c}')
