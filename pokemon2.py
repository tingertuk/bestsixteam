# Projeto Pokemon - Main
# Goal: find out the best combination of 6 pokemon for a team.
# tiaaagosr@gmail.com

pkmn = {}
tipo = {}
tipoGuia = {}
cnt = 1

for line in open('pkmnstats.csv'):
    ind = line.split(',')
    ind[-1] = ind[-1].strip()
    pkmn[ind[0]] = ind[1:]
    for i in range(3,11):
        pkmn[ind[0]][i] = float(pkmn[ind[0]][i])

for line in open('typechart.csv'):
    typ = line.split(',')
    tipo[typ[0]] = typ[1:]
    tipoGuia[typ[0]] = cnt
    cnt += 1
    for i in range(0,18):
        tipo[typ[0]][i] = float(tipo[typ[0]][i])
        
import random


fighters = random.sample(list(pkmn.keys())[0:10],2)
pkmnA = pkmn[fighters[0]]
pkmnB = pkmn[fighters[1]]
modA = [1,1]
modB = [1,1]

# just for fun

# pkmnA = pkmn['26']
# pkmnB = pkmn['9']



if pkmnA[2]=='':
    iMax = 2
    modA[1] = 0
else:
    iMax = 3


if pkmnB[2]=='':
    jMax = 2
    modB[1] = 0
else:
    jMax = 3


for i in range(1,iMax):
    for j in range(1,jMax):
        modA[i-1] *= tipo[pkmnA[i]][tipoGuia[pkmnB[j]]-1]

for j in range(1,jMax):
    for i in range(1,iMax):
        modB[j-1] *= tipo[pkmnB[j]][tipoGuia[pkmnA[i]]-1]



while pkmnB[3] >= 0 and pkmnA[3] >= 0:
    damagePh = ((22 * 60 * (pkmnA[4]/pkmnB[5]))/50) * max(modA)
    damageSp = ((22 * 60 * (pkmnA[6]/pkmnB[7]))/50) * max(modA)

    if damagePh >= damageSp:
        pkmnB[3] = pkmnB[3] - damagePh
    else:
        pkmnB[3] = pkmnB[3] - damageSp

    damagePh = ((22 * 60 * (pkmnB[4]/pkmnA[5]))/50) * max(modB)
    damageSp = ((22 * 60 * (pkmnB[6]/pkmnA[7]))/50) * max(modB)

    if damagePh >= damageSp:
        pkmnA[3] = pkmnA[3] - damagePh
    else:
        pkmnA[3] = pkmnA[3] - damageSp


print(pkmnA)
print(pkmnB)

# amanha:
# computar/tabelar as vitorias
# add clausula pra qnd os dois caem pra menos de 0, maior speed vencer

    
