import numpy as np

fitxer = open('input.txt', 'r')

files = fitxer.readlines()

max_fil = 99
max_col = 99

# create matrix with zeroes
matriu = np.zeros((max_fil,max_col),dtype=int)

for indexFila, linea in enumerate(files):
    for indexColumna, caracter in enumerate(linea[:-1]):
        matriu[indexFila][indexColumna] = int(caracter)

suma_arbres = 0
for fila in range(1, max_fil - 1):
    for columna in range(1, max_col - 1):
        arbre = matriu[fila, columna]
        esquerra = matriu[fila, 0:columna]
        dreta = matriu[fila, columna+1:]
        dalt = matriu[0:fila, columna]
        baix = matriu[fila+1:, columna]

        if all(arbre > i for i in esquerra):
            # print('Esquerra: ', esquerra, '-', arbre)
            suma_arbres = suma_arbres + 1
        elif all(arbre > i for i in dreta):
            # print('Dreta: ', arbre, '-', dreta)
            suma_arbres = suma_arbres + 1
        elif all(arbre > i for i in dalt):
            # print('Dalt: ', dalt, '-', arbre)
            suma_arbres = suma_arbres + 1
        elif all(arbre > i for i in baix):
            # print('Baix: ', arbre, '-', baix)
            suma_arbres = suma_arbres + 1

edge = 99*2 +97*2
print('How many trees are visible from outside the grid? ', suma_arbres+edge)

arbres_escenic = 0

for fila in range(1, max_fil - 1):
    for columna in range(1, max_col - 1):
        arbre = matriu[fila, columna]
        esquerra = matriu[fila, 0:columna]
        dreta = matriu[fila, columna+1:]
        dalt = matriu[0:fila, columna]
        baix = matriu[fila+1:, columna]

        esquerra_esc = 0
        dreta_esc = 0
        dalt_esc = 0
        baix_esc = 0

        # print('Esquerra: ', esquerra, '-', arbre, ':', len(esquerra))
        alreves = np.flip(esquerra)
        for fulla in alreves:
            # print('Alreves: ', alreves, '-', arbre, ':', fulla)
            if arbre > fulla:
                esquerra_esc = esquerra_esc + 1
            else:
                esquerra_esc = esquerra_esc + 1
                break
                # print('Esquerra: ', esquerra, '-', esquerra_esc)                                
        # print('Trobats: ', esquerra, '-', arbre, '->', esquerra_esc)
        for fulla in dreta:
            # print('Alreves: ', alreves, '-', arbre, ':', fulla)
            if arbre > fulla:
                dreta_esc = dreta_esc + 1
            else:
                dreta_esc = dreta_esc + 1
                break
        # dalt
        alreves = np.flip(dalt)
        for fulla in alreves:
            # print('Alreves: ', alreves, '-', arbre, ':', fulla)
            if arbre > fulla:
                dalt_esc = dalt_esc + 1
            else:
                dalt_esc = dalt_esc + 1
                break
        # baix        
        for fulla in baix:
            # print('Alreves: ', alreves, '-', arbre, ':', fulla)
            if arbre > fulla:
                baix_esc = baix_esc + 1
            else:
                baix_esc = baix_esc + 1
                break

        # print("Valors escenics: ",esquerra_esc, '-', dreta_esc, '-', dalt_esc, '-', baix_esc)
        producte = esquerra_esc * dreta_esc * dalt_esc * baix_esc
        if producte > arbres_escenic:
            arbres_escenic = producte

print('What is the highest scenic score possible for any tree? ', arbres_escenic)
