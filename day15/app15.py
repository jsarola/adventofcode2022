file = 'input.txt'
logging = False

fitxer = open(file, 'r')
files = fitxer.readlines()

taula = {}

def omplirManhattan(posX, posY, espai):
    global esquerra
    global dreta
    for columna in range(espai*-1, espai + 1):
        for fila in range(espai*-1, espai + 1):
            if (abs(columna) + abs(fila)) <= espai:
                try:
                    valor = taula[posX + columna, posY + fila]
                except:
                    valor = 0
                if valor == 0:
                    taula[posX + columna, posY + fila] = '#'
                    if esquerra > (posX + columna):
                        esquerra = posX + columna
                    if dreta < (posX + columna):
                        dreta = posX + columna

esquerra = 10000000
dreta = 0

for indexFila, linea in enumerate(files):
    print('Fila ', indexFila)
    cadena = linea.split()
    sensorX = int(cadena[2][:-1].split('=')[1])
    sensorY = int(cadena[3][:-1].split('=')[1])
    beaconX = int(cadena[8][:-1].split('=')[1])
    beaconY = int(cadena[9].split('=')[1])

    taula[sensorX, sensorY] = 'S'
    taula[beaconX, beaconY] = 'B'

    cols = [sensorX, beaconX]
    colsSorted = sorted(cols, reverse = True)
    # print(colsSorted)
    fils = [sensorY, beaconY]
    filsSorted = sorted(fils, reverse = True)
    # print(filsSorted)

    espaitmp = (colsSorted[0] - colsSorted[1]) + (filsSorted[0] - filsSorted[1])
    
    omplirManhattan(sensorX, sensorY, espaitmp)

# print(taula)
print('Més esquerra ', esquerra)
print('Més dreta ', dreta)

fila = 10
positions = 0
for columna in range(esquerra, dreta + 1):            
    try:
        valor = taula[columna, fila]
    except:
        valor = 'X'
    print(columna, '->', valor)
    if valor == '#':
        positions = positions + 1

print('In the row where y=', fila, ', how many positions cannot contain a beacon? ', positions)

        

