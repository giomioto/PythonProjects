conta = str(input('Digite sua expressão matemática: '))
qnt = list()
for i in conta:
    if i == "(":
        qnt.append('(')
    elif i == ')':
        if len(qnt) > 0:
            qnt.pop()
        else:
            qnt.append(')')
            break
if len(qnt) == 0:
    print('Sua expressãoestá correta! ')
else:
    print('Sua expressão está incorreta! ')