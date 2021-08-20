listnum = []
while True:
    listnum.append(int(input('Digite um numero: ')))
    escolha = str(input('Quer digitar outro?  [s/n]: '))    
    if escolha not in 'Ss':
        break
print('=-'*40)
listnum.sort()
print(f'Voce digitou os valores {listnum}')

