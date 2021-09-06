from random import randint
numeros = (randint(1,100), randint(1,100),randint(1,100),randint(1,100),randint(1,100))
print(f'Os valores sorteados foram ', end=" ")
for n in numeros:
    print(f'{n} ', end=' ')
print(f'\nO menor valor é {min(numeros)}')
print(f'O maior valor é {max(numeros)}')





"""""""""""""""""""""
import random
a = (random.randint(0,100))
b = (random.randint(0,100))
c = (random.randint(0,100))
d = (random.randint(0,100))
e = (random.randint(0,100))
todos = (a, b, c, d, e)
print(f'Os valores sorteados foram {todos}')
print(f'O menor valor é {min(todos)}')
print(f'O maior valor é {max(todos)}')
"""""""""""""""""""""
