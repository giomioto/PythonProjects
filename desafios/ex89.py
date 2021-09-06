from time import sleep
princ = list()
while True:
    nome=(str(input('Nome: ')))
    nota1=(float(input('Nota 1: ')))
    nota2=(float(input('Nota 2: ')))
    media=(nota1+nota2)/2
    princ.append([nome, [nota1, nota2], media])
    escolha = str(input('Quer continuar? [s/n] '))
    if escolha in "Nn":
        break
print('-*-'*30)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(princ):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:    
    qual = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if qual != len(princ)-1:
        print(f'O aluno {qual} não está cadastrado')
    if qual == 999:
            print('Finalizando...')
            sleep(1)
            print('VOLTE SEMPRE!')
            break
    if qual <= len(princ)-1:
        print(f'Notas de {princ[qual][0]} são {princ[qual][2]}')