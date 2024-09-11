v1 = int(input('Insira um valor: '))
v2 = int(input('Insira outro valor: '))
v3 = int(input('Insira o último valor: '))

high = v1
mid = v2
low = v3

if v1 > v2 and v2 > v3:
    high = v1
    mid = v2
    low = v3
elif v1 > v3 and v3 > v2:
    high = v1
    mid = v3
    low = v2
elif v3 > v1 and v1 > v2:
    high = v3
    mid = v1
    low = v2
elif v3 > v2 and v2 > v1:
    high = v3
    mid = v2
    low = v1
elif v2 > v1 and v1 > v3:
    high = v2
    mid = v1
    low = v3
else:
    high = v2
    mid = v3
    low = v1

print(f'A ordem decrescente dos números é {high, mid,low}')
