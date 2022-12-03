fitxer = open('input.txt', 'r')

files = fitxer.readlines()

import string
import difflib

valors = {}

index = 1
for a in string.ascii_lowercase:
    valors[a] = index
    index = index + 1

for a in string.ascii_uppercase:
    valors[a] = index
    index = index + 1

suma_1 = 0

for fila in files:
    mig = int(len(fila)/2)
    firstpart, secondpart = fila[:mig], fila[mig:]
    for c in firstpart:
        if c in secondpart:
            trobat = c
            suma_1 = suma_1 + valors[c]
            break

print('What is the sum of the priorities of those item types? ', suma_1)

suma_2 = 0
index = 1
for fila in files:
    if index == 1:
        fila1 = fila[:-1]
        index = index + 1
    elif index == 2:
        fila2 = fila[:-1]
        index = index + 1
    elif index == 3:
        fila3 = fila[:-1]
        index = 1
        for c in fila1:
            if c in fila2:
                if c in fila3:
                    trobat = c
                    suma_2 = suma_2 + valors[c]
                    break

print('What is the sum of the priorities of those item types? ', suma_2)