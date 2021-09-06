palavras = (str(input('Digite uma palavra sem acentos: ')),
str(input('Digite uma palavra sem acentos: ')),
str(input('Digite uma palavra sem acentos: ')),
str(input('Digite uma palavra sem acentos: ')),
str(input('Digite uma palavra sem acentos: ')))


for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')