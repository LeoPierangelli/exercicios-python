a = int(input('Quantas maçãs vc comprou?\n-> '))
if a>=12:
    a = a*0.30
    print(f'você gastou R${a}')
else:
    a = a*0.25
    print(f' você gastou R${a}')