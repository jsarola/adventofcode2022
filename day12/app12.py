file = 'test.txt'
logging = True

def adjunts(H,T):
    llistaAdjunts = []
    for i in [-1,0,1]:
        for y in [-1,0,1]:
            llocFila = H[0]+i
            llocColumna = H[1]+y
            llistaAdjunts.append([llocFila, llocColumna])
    
    # print('Llista adjunst: ','(', H, ',', T, ') ', llistaAdjunts)
    if T in llistaAdjunts:
        return True
    else:
        return False

fitxer = open(file, 'r')

files = fitxer.readlines()

matriu = []

# create matrix
for indexFila, linea in enumerate(files):
    matriu.append([])
    for indexColumna, caracter in enumerate(linea[:-1]):
        numero = ord(caracter) - 96
        if caracter == 'S':
            start = [indexFila, indexColumna]
            numero = 0
        elif caracter == 'E':
            stop = [indexFila, indexColumna]
            numero = 27
        matriu[indexFila].append(numero)

if logging: print(matriu, start, stop)

llista_accessos = []


def buscarSeguent(fila, columna):
    return [fila, columna + 1]

def buscarEnd(fila, columna, caracter):
    if matriu[fila-1][columna] == caracter:
        return True
    elif matriu[fila+1][columna]== caracter:
        return True
    elif matriu[fila][columna-1] == caracter:
        return True
    elif matriu[fila][columna+1] == caracter:
        return True
    else:
        return False

def buscarSolucio(inici):
    if buscarEnd(inici[0],inici[1],2):
        llista_accessos.append([inici[0],inici[1]]) 
        return True
    else:
        seguent = buscarSeguent(inici[0],inici[1])
        if seguent == [-1,-1]:
            return False
        else:
            llista_accessos.append([inici[0],inici[1]]) 
            if buscarSolucio(seguent):
                return True
            else:
                return False

    # if posicio in llista_accessos:
    #    return False
    #    llista_accessos.append(posicio)

print(buscarSolucio(start))


print(llista_accessos)