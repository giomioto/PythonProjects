listnum = []
while True:
    listnum.append(int(input('Digite um numero: ')))
    r = str(input('Quer continuar?[S/N]: '))
    if r not in "Ss":
        break
print(f'Você digitou {len(listnum)} elementos')
listnum.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram {listnum}')
if 5 in listnum:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista')