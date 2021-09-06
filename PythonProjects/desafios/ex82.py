listnum = []
pares = []
impares = []
while True:
    aux = listnum.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta not in 'Ss':
        break
print(f'A lista comepleta é {listnum}') 

for i, v in enumerate(listnum):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista dos pares é: {pares}')
print(f'A lista dos impares é: {impares}')
