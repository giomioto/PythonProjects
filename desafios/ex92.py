from datetime import datetime
pessoa = dict()
pessoa["nome"] = str(input('NOME: '))
nasc = int(input("ANO DE NASCIMENTO: "))
pessoa["idade"] = datetime.now().year - nasc
pessoa["carteira"] = int(input("CARTEIRA DE TRABALHO (0 não tem): "))
if pessoa["carteira"] !=0:
    pessoa["contratacao"] = int(input("ANO DE CONTRATAÇÂO: "))
    pessoa["salario"] = float(input("Salário: R$"))
    pessoa["aposentadoria"] = pessoa["idade"] + ((pessoa["contratacao"] + 35) - datetime.now().year)
print('-='*30)
for i, v in pessoa.items():
    print(f' - {i} tem o valor {v} ')