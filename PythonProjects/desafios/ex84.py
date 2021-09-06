temp = list()
nomes =  list()
mai = men =0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(nomes) == 0:
        mai = men = temp[1]
    else:
        if temp[1]>mai:
            mai = temp[1]
        if temp[1]<men:
            men= temp[1]
    nomes.append(temp[:])
    temp.clear()
    escolha = str(input('Quer continuar? [S/N]: ')).lower()
    if escolha in "n":
        break
    print('-'*20)
print('='*60)
print(f"Ao todo, você cadastrou {len(nomes)} pessoas")
print(f'O maior peso cadastrado foi de {mai}Kg. Peso de ', end="")
for p in nomes:
    if p[1]==mai:
        print(f'[{p[0]}] ')
print(f'O menor peso cadastrado foi de {men}Kg. Peso de ',end="")
for p in nomes:
    if p[1]==men:
        print(f'[{p[0]}] ',end="")
