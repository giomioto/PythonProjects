numeros = []
mai = 0
men = 0

for c in range(0, 5):
    numeros.append(int(input(f'Digite um número na posição {c}:  ')))
    if c == 0:
        mai = men = numeros[c]
    else:
        if numeros > mai:
            mai = numeros
        if numeros <  men:
            men = numeros
print('=-'*30)
print(f'Voce digitou os valores {numeros}')
print(f'O maior numero digitado foi {mai}') 
for i, v in enumerate (numeros):
    if numeros(i) == mai:
        print(f'{i}... ',end='')
print(f'O maior numero digitado foi {men} ',end='')
for i, v in enumerate (numeros):
    if numeros(v) == men:
        print(f'{i}... ',end='')
print()