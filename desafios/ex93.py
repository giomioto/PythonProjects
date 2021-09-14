jogo = dict()
gols = list()
jogo["nome"]=str(input("nome do jogador: "))
partidas=int(input("Quantas partidas ele jogou? "))
for c in range(partidas):
    gols.append(int(input(f"Quantos gols na partida {c}: ")))
jogo["scores"] = gols[:]
jogo['total']= sum(gols)
print("-="*30)
print(jogo)
print("-="*30)
for i, v in jogo.items():
    print(f"O campo {i} tem valor {v}")
print("-="*30)
for p, g in enumerate (jogo["scores"]):
    print(f"O jogador jogou {partidas} partidas")
    print(f"    => Na partida {p}, fez {g} gols")
print(f"Foi um total de {jogo['total']} gols")