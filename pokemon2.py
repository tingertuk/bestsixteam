# Projeto Pokemon - Main
# Goal: find out the best combination of 6 pokemon for a team.
# tiaaagosr@gmail.com

pkmn = {}
tipo = {}
tipoGuia = {}
cnt = 1

# Creates the 'pkmn' dictionary. Each entrance, from '1' to '802' represents a Pokémon. The Dictionary contains the pokémon name, type(s) and stats.
# Stats are, in order, HP, Attack, Defensa, Sp.Atk, Sp.Def, Speed, Total Stats Point, Average Stats Point
for line in open('pkmnstats.csv'):
    ind = line.split(',')
    ind[-1] = ind[-1].strip()
    pkmn[ind[0]] = ind[1:]
    for i in range(3,11):
        pkmn[ind[0]][i] = float(pkmn[ind[0]][i])

# Creates the 'tipo' dictionary. Each entrance contains information effectiveness of an attack. Each entrance is a vector with an "Effectiveness Modifier."
# Also creates the 'tipoGuia' dictionary. Each entrance links a type name (e.g. 'Water') to an index number (e.g. 11), representing the location of the type in the 'guia' dictionary. Allows calculation of type effectiveness.
for line in open('typechart.csv'):
    typ = line.split(',')
    tipo[typ[0]] = typ[1:]
    tipoGuia[typ[0]] = cnt
    cnt += 1
    for i in range(0,18):
        tipo[typ[0]][i] = float(tipo[typ[0]][i])
        
def battle(fighter1, fighter2):
    "This function will be used to simulate the battle between 2 pokémon."

    
    # First, load the two dueling pokémon into the function and create blank effectiveness modifier for them.
    pkmnA = pkmn[fighter1]
    pkmnB = pkmn[fighter2]

    modA = [1,1]
    modB = [1,1]

    # Modifier the effectiveness modifiers based on the types of the dueling pokémon and create index maximuns for checking types during the battles.
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

    # The battle simulator itself. Runs until at least of the fighting pokémon is knocked down to 0 or below.
    # It uses the type modifiers, compares Atk-Def and SpA-SpD and use the highest (strongest) option.
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

    if pkmnA[3] <= 0 and pkmnB[3] < 0:
        if pkmnA[8] < pkmnB[8]:
            winner = pkmnB[0]
        else:
            winner = pkmnA[0]

    else:
        if pkmnA[3] <= 0:
            winner = pkmnB[0]
        else:
            winner = pkmnA[0]
    


    print(pkmnA)
    print(pkmnB)
    print('The winner is: ' + winner)
    return

import random
fighters = random.sample(list(pkmn.keys())[0:10],2)

battle(fighters[0], fighters[1])

# amanha:
# computar/tabelar as vitorias

    
