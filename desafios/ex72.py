numero = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
          'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    escolha = int(input('Digite um número de 0 à 20: '))
    if 0<= escolha <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Você digitou o número {numero[escolha]}')