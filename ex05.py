'''v1 = int(input('Insira um valor: '))
v2 = int(input('Insira outro valor: '))
v3 = int(input('Insira o último valor: '))
high = v1
mid = v2
low = v3

if v2 > high:
    high = v2
    if v3 > mid:
        v3 = mid
    else:
        v3 = low
if v3 > high:
    high = v3
    if v2 > mid:
        mid = v2
    else:
        v1 = low



print(f'A ordem crescente dos números é {low, mid, high}')'''



v1 = int(input('Insira um valor: '))
v2 = int(input('Insira outro valor: '))
v3 = int(input('Insira o último valor: '))

high = v1
if v2 > high:
    v2 = high
if v3 > high:
    v3 = high

low = v1
if v2 < low:
    v2 = low
if v2 < low:
    v3 = low
mid = v1 + v2 + v3 - high - low
print(high, mid, low)
