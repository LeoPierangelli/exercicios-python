'''a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite o último valor: '))

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)
'''

#GARABITO
a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite o último valor: '))

high = a

if b > high:
    high = b
if c > high:
    high = c

print(f'{high}')
