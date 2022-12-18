file = 'test.txt'
#file = 'input.txt'
logging = True

fitxer = open(file, 'r')
files = fitxer.readlines()

taula = {}

def omplirTimesquare(posX, posY, espai, laFila):
    global esquerra
    global dreta
    fila = laFila
    if fila in range(posY+(espai*-1), posY+espai+1):
        if fila >= posY:
            espaiFila = espai - (fila - posY)
        else:
            espaiFila = espai - (posY - fila)
        for columna in range(espaiFila*-1, espaiFila + 1):            
            try:
                valor = taula[posX + columna, fila]
            except:
                valor = 0
            if valor == 0:
                print(columna, fila)
                taula[posX + columna, fila] = '#'
                if esquerra > (posX + columna):
                    esquerra = posX + columna
                if dreta < (posX + columna):
                    dreta = posX + columna


esquerra = 10000000
dreta = 0

filaBuscar = 10
# filaBuscar = 2000000

for indexFila, linea in enumerate(files):
    break
    # if logging: print('Fila ', indexFila)
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
    
    omplirTimesquare(sensorX, sensorY, espaitmp, filaBuscar)
    # omplirManhattan(sensorX, sensorY, espaitmp)

# print(taula)
print('Més esquerra ', esquerra)
print('Més dreta ', dreta)

positions = 0
for columna in range(esquerra, dreta + 1):

    try:
        valor = taula[columna, filaBuscar]
    except:
        valor = 'X'
    if logging: print(columna, '->', valor)
    if valor == '#':
        positions = positions + 1

print('In the row where y=', filaBuscar, ', how many positions cannot contain a beacon? ', positions)


# HowTo
# Recurse find if position is occupied by all rules

class Quadrat:
    def __init__(self, posEsquerra, posDreta, posDalt, posBaix):
        self.posEsquerra = posEsquerra
        self.posDreta = posDreta
        self.posDalt = posDalt
        self.posBaix = posBaix

    def esquerra(self):
        return self.posEsquerra

    def dreta(self):
        return self.posDreta

    def dalt(self):
        return self.posDalt

    def baix(self):
        return self.posBaix

    def quadratMinim(self):
        esMinim = False
        if self.posDreta - self.posEsquerra == 1:
            esMinim = True
            if self.posBaix - self.posDalt == 1:
                esMinim = True
        return esMinim
    
    def indexQuadrat(self):
        return ([self.posDreta, self.posBaix])

def posicioLliure(posicio):
    posX = posicio[0]
    posY = posicio[1]
    laPosicio = False

    rules = []

    for check in rules:
        columna = check[0]
        fila = check[1]
        espai = check[2]
        if posY in range(fila+(espai*-1), fila*espai+1):
            if fila >= posY:
                espaiFila = espai - (fila - posY)
            else:
                espaiFila = espai - (posY - fila)
            if posX in range(columna+(espaiFila*-1), columna+espaiFila+1):            
                laPosicio = True
    return laPosicio

def buscarForat(taulell):
    if taulell.quadratMinim():
        if logging: print('Taulell: ', vars(taulell))
        if logging: print('Taulell minim: ', taulell.indexQuadrat())
        if posicioLliure(taulell.indexQuadrat()):
            return False
    else:
        ampla = (taulell.dreta() - taulell.esquerra()) // 2
        amplaResidu = (taulell.dreta() - taulell.esquerra()) % 2
        llarg = (taulell.baix() - taulell.dalt()) // 2
        llargResidu = (taulell.baix() - taulell.dalt()) % 2
        print('ampla', ampla, amplaResidu)
        print('llarg', llarg, llargResidu)
        for i in range(0,2):
            for j in range(0,2):
                newEsquerra = taulell.esquerra() + i*ampla
                newDreta = newEsquerra + ampla + i*amplaResidu
                newDalt = taulell.dalt() + j*llarg + j*llargResidu
                newBaix = newDalt + llarg + j*llargResidu
                noutaulell = Quadrat(newEsquerra, newDreta, newDalt, newBaix)
                if logging: print('Nou ', vars(noutaulell))
                beaconPossible = buscarForat(noutaulell)                
    return ([-1,-1])


minCoordinates = 0
maxCoordinates = 20
# minCoordinates = 0
# maxCoordinates = 4000000

elmeutaulell = Quadrat(minCoordinates,maxCoordinates,minCoordinates,maxCoordinates)

rules = []
# Create list rules
for indexFila, linea in enumerate(files):
    # if logging: print('Fila ', indexFila)
    cadena = linea.split()
    sensorX = int(cadena[2][:-1].split('=')[1])
    sensorY = int(cadena[3][:-1].split('=')[1])
    beaconX = int(cadena[8][:-1].split('=')[1])
    beaconY = int(cadena[9].split('=')[1])

    cols = [sensorX, beaconX]
    colsSorted = sorted(cols, reverse = True)
    # print(colsSorted)
    fils = [sensorY, beaconY]
    filsSorted = sorted(fils, reverse = True)
    # print(filsSorted)

    espaitmp = (colsSorted[0] - colsSorted[1]) + (filsSorted[0] - filsSorted[1])
    
    rules.append([sensorX, sensorY, espaitmp])

if logging: print(rules)

beaconPossible = buscarForat(elmeutaulell)

columnaBeacon = beaconPossible[0]
filaBeacon = beaconPossible[1]
if logging: print('Columna: ', columnaBeacon, ' Fila: ', filaBeacon)
           
tuninFreq = columnaBeacon * 4000000 + filaBeacon
        
print('What is its tuning frequency? ', tuninFreq)
