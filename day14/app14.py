file = 'test.txt'
logging = True

fitxer = open(file, 'r')
files = fitxer.readlines()

mapa = {}

sota = 0

for indexFila, linea in enumerate(files):
    cadena = linea[:-1].split('->')
    fil = []
    for posicio in cadena:
        posiciotmp = posicio.split(',')
        fil.append([int(posiciotmp[0]), int(posiciotmp[1])])

    for i in range(1, len(fil)):        
        posicionsX = [fil[i-1][0], fil[i][0]]
        posicionsXsorted = sorted(posicionsX)        
        for x in range(posicionsXsorted[0], posicionsXsorted[1]+1):
            posicionsY = [fil[i-1][1], fil[i][1]]
            posicionsYsorted = sorted(posicionsY)
            for y in range(posicionsYsorted[0], posicionsYsorted[1]+1):
                if sota < y:
                    sota = y
                mapa[x, y] = 1

if logging: print('Ultima fila ', sota)

# used by part 2
mapa2 = mapa.copy()

def omplirSorra(posX, posY):
    ultimaposicio = posY
    if posY + 1 > sota:
        return ultimaposicio + 1
    
    try:
        valor = mapa[posX, posY + 1]
    except:
        valor = 0    
    if valor >= 1:
        try:
            valor = mapa[posX - 1, posY + 1]
        except:
            valor = 0    
        if valor >= 1:
            try:
                valor = mapa[posX + 1, posY + 1]
            except:
                valor = 0    
            if  valor >= 1:
                mapa[posX, posY] = 2
                return posY
            else:
                ultimaposicio = omplirSorra(posX + 1, posY + 1)
                return ultimaposicio
        else:
            ultimaposicio = omplirSorra(posX - 1, posY + 1)
            return ultimaposicio
    else:
        ultimaposicio = omplirSorra(posX, posY + 1)
    
    return ultimaposicio

sorra = 0
posSorra = 0

while sota > posSorra:
    posSorra = omplirSorra(500,0)
    if sota > posSorra:
        sorra = sorra + 1
        # print('sorra ', sorra, ' -> ', mapa)

if logging: print('Gra de sorra numero ', sorra)
if logging: print('Mapa ', mapa)
print('How many units of sand come to rest before sand starts flowing into the abyss below? ', sorra)

def omplirSorra2(posX, posY):
    ultimaposicio = posY
    if posY + 1 > sota:
        return ultimaposicio + 1
    
    try:
        valor = mapa2[posX, posY + 1]
    except:
        valor = 0    
    if valor >= 1:
        try:
            valor = mapa2[posX - 1, posY + 1]
        except:
            valor = 0    
        if valor >= 1:
            try:
                valor = mapa2[posX + 1, posY + 1]
            except:
                valor = 0    
            if  valor >= 1:
                mapa2[posX, posY] = 2
                return posY
            else:
                ultimaposicio = omplirSorra2(posX + 1, posY + 1)
                return ultimaposicio
        else:
            ultimaposicio = omplirSorra2(posX - 1, posY + 1)
            return ultimaposicio
    else:
        ultimaposicio = omplirSorra2(posX, posY + 1)
    
    return ultimaposicio

sorra = 0
posSorra = 1
sota = sota + 2

while posSorra > 0:
    posSorra = omplirSorra2(500,0)
    sorra = sorra + 1
    print('sorra ', sorra, ' -> ', mapa2)

if logging: print('Gra de sorra numero ', sorra)
if logging: print('Mapa ', mapa2)