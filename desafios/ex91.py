from random import randint
from time import sleep
from operator import itemgetter
jogo = {"Jogardor1": randint(1,6),
        "Jogardor2": randint(1,6),
        "Jogardor3": randint(1,6),
        "Jogardor4": randint(1,6),}
print('VALORES SORTEADOS: ')
ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
print('='*30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'  ===RANKING DOS SORTEADOS===')
for i, j in enumerate(ranking):
    print(f'{i+1}° Lugar: {j[0]} com {j[1]}')
    sleep(1)

