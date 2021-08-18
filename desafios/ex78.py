numeros = []
maior = 0
menor = 0

for c in range(0, 5):
    numeros.append(int(input(f'Digite um número na posição {c}:  ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] <  menor:
            menor = numeros[c]
print('=-'*30)
print(f'Voce digitou os valores {numeros}')
print(f'O maior numero digitado foi {maior} na posição ',end='') 
for i, v in enumerate (numeros):
    if v == maior:
        print(f'{i}... ',end='\n')
print(f'O maior numero digitado foi {menor} na posição ',end='')
for i, v in enumerate (numeros):
    if v == menor:
        print(f'{i}... ',end='')
print()
