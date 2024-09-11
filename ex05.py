v1 = int(input('Insira um valor: '))
v2 = int(input('Insira outro valor: '))
v3 = int(input('Insira o último valor: '))
high = v1
mid = v2
low = v3

if v2 > v1 and v2 > v3:
    high = v2
elif v3 > v1 and v3 > v2:
    high = v3
elif v1 < v2 and v1 < v3:
    low =
print(f'A ordem crescente dos números é {low, mid, high}')
