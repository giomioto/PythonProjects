from random import randint
from time import sleep
mega=list()
jogos = list()
print('-='*30)
print('                     JOGO DA MEGA SENA      ')
print('-='*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot=1
while tot <= quant:
    cont=0
    while True:
        num = randint(0,60)
        if num not in mega:
            mega.append(num)
            cont +=1
        if cont >= 6:
            break
    mega.sort()
    jogos.append(mega[:])
    mega.clear()
    tot+=1
print('-='*6,f'Sorteando {quant} jogos','-='*6)
for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')
    sleep(1)
print('-='*8,f'BOA SORTE!','-='*8)