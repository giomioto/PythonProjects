times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print(f'Os times do Brasileirão:{times}')
print('-='*30)

print(f'Os primeiros 5 colocados do Brasileirão: {times[0:4]}')
print('-='*30)

print(f'Os ultimos 4 colocados do Brasileirão: {times[15:19]}')
print('-='*30)

print(f'Os times em ordem alfabética: {sorted(times)}')
print('-='*30)

print(f'O Atlético-PR está na {times.index("Atlético-PR")+1}° posição')
print(('-='*30))