todo =  [[], []]
n = 0
for c in range(1,8):
    n=int(input(f'Digite o {c}° numero: '))
    if n % 2 == 0:
        todo[0].append(n)
    else:
        todo[1].append(n)
print('='*60)
todo[0].sort()
todo[1].sort()
print(f'Os valores pares digitados foram {todo[0]}')
print(f'Os valores impares digitados foram {todo[1]}')