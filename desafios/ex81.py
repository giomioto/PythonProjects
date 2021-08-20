cont = 0
listnum = []
while True:
    listnum.append(int(input('Digite um numero: ')))
    r = str(input('Quer continuar?[S/N]: '))
    cont +=1
    if r not in "Ss":
        break
ordem = sorted(listnum, reverse = True)
print(f'Você digitou {cont} elementos')
print(f'Os valores digitados em ordem decrescente foram {ordem}')
if 5 in listnum:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista')