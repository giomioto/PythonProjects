num = (int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')))
print(f'Voce digitou os números {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 foi digitado na {num.index(3)}° posição')
else:
    print('O valor três não foi digitado nenhum vez')
print(f'Os valores pares foram ',end='')
for n in num:
    if n % 2 == 0:
        print(f'Os valores pares foram ',end='')
        print(n, end=' ')
else:
    print('0')
