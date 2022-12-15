file = 'test.txt'
logging = False

fitxer = open(file, 'r')
files = fitxer.readlines()

taula = {}

def omplirManhattan(posX, posY, espai):
    for fila in range(espai*-1, espai + 1):
        for columna in range(espai*-1, espai + 1):            
            if (abs(fila) + abs(columna)) <= espai:
                try:
                    valor = taula[posX + fila, posY + columna]
                except:
                    valor = 0
                if valor == 0:
                    taula[posX + fila, posY + columna] = '#'                    

for indexFila, linea in enumerate(files):
    cadena = linea.split()
    sensorX = int(cadena[2][:-1].split('=')[1])
    sensorY = int(cadena[3][:-1].split('=')[1])
    beaconX = int(cadena[8][:-1].split('=')[1])
    beaconY = int(cadena[9].split('=')[1])
    print(sensorX,sensorY,beaconX,beaconY)



omplirManhattan(5,2,3)

print(taula)
