print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
total = int(input('Quanto você gostaría de sacar ? R$ '))
ced = 50
cedulas = [50, 20, 10, 1]
totced = 0

"""
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas do valor de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
"""
i = 0
totced = 0

while i < 4:
    if total >= cedulas[i]:
        totced = total // cedulas[i]
        total %= cedulas[i]
        print(f'Total de {totced} cédulas do valor de R${cedulas[i]}')
    i += 1


print('='*30)
print('Volte sempre ao BANCO CEV, tenha um bom dia!')
