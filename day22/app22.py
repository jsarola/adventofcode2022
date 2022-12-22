file = 'input.txt'
logging = True

fitxer = open(file, 'r')
files = fitxer.readlines()

# test
# maxFila = 12
# maxColumna = 16

# input
maxFila = 200
maxColumna = 150


import numpy as np


# create matrix with zeroes
taula = np.zeros([maxFila,maxColumna], dtype='U1')

fila = 0
for indexFila, linea in enumerate(files):
    columna = 0
    if 'R' in linea:
        lineamoviments = linea[:-1]
        break
    for caracter in linea[:-1]:
        if caracter == '.':
            taula[fila, columna] = '.'
        elif caracter == '#':
            taula[fila, columna] = '#'
        else:
            taula[fila, columna] = ''
        columna = columna + 1
    fila = fila + 1

moviments = []

cadena = ''
for caracter in lineamoviments:
    if caracter.isnumeric():
        cadena = cadena + caracter
    else:
        elmoviment = caracter
        moviments.append(int(cadena))
        moviments.append(elmoviment)
        cadena = ''

if cadena != '':
    moviments.append(int(cadena))

if logging: print('Taula: ', taula)
if logging: print('Moviments: ', moviments)

def trobarInici():
    fil = 0
    for i in range(0, maxColumna):
        if taula[0, i] == '.':
            col = i
            break
        elif taula[0,i] == '#':
            col = i
            break
    return (fil,col)

def moureDreta(pos):
    global posicioInicial

    posicioSeguent = (posicioInicial[0], posicioInicial[1])
    for i in range(0,pos):
        posicioSeguent = (posicioSeguent[0], (posicioSeguent[1] + 1) % maxColumna)
        while taula[posicioSeguent[0], posicioSeguent[1]] == '':
            posicioSeguent = (posicioSeguent[0], (posicioSeguent[1] + 1) % maxColumna)
        if taula[posicioSeguent[0], posicioSeguent[1]] == '.':
            posicioInicial = (posicioSeguent[0], posicioSeguent[1])
        elif taula[posicioSeguent[0], posicioSeguent[1]] == '#':
            break
    return

def moureBaix(pos):
    global posicioInicial

    posicioSeguent = (posicioInicial[0], posicioInicial[1])
    for i in range(0,pos):
        posicioSeguent = ((posicioSeguent[0] + 1) % maxFila, posicioSeguent[1])
        while taula[posicioSeguent[0], posicioSeguent[1]] == '':
            posicioSeguent = ((posicioSeguent[0] + 1) % maxFila, posicioSeguent[1])
        if taula[posicioSeguent[0], posicioSeguent[1]] == '.':
            posicioInicial = (posicioSeguent[0], posicioSeguent[1])
        elif taula[posicioSeguent[0], posicioSeguent[1]] == '#':
            break

    return

def moureEsquerra(pos):
    global posicioInicial

    posicioSeguent = (posicioInicial[0], posicioInicial[1])
    for i in range(0,pos):
        posicioSeguent = (posicioSeguent[0], (posicioSeguent[1] - 1) % maxColumna)
        while taula[posicioSeguent[0], posicioSeguent[1]] == '':
            posicioSeguent = (posicioSeguent[0], (posicioSeguent[1] - 1) % maxColumna)
        if taula[posicioSeguent[0], posicioSeguent[1]] == '.':
            posicioInicial = (posicioSeguent[0], posicioSeguent[1])
        elif taula[posicioSeguent[0], posicioSeguent[1]] == '#':
            break
    return

def moureDalt(pos):
    global posicioInicial

    posicioSeguent = (posicioInicial[0], posicioInicial[1])
    for i in range(0,pos):
        posicioSeguent = ((posicioSeguent[0] - 1) % maxFila, posicioSeguent[1])
        while taula[posicioSeguent[0], posicioSeguent[1]] == '':
            posicioSeguent = ((posicioSeguent[0] - 1) % maxFila, posicioSeguent[1])
        if taula[posicioSeguent[0], posicioSeguent[1]] == '.':
            posicioInicial = (posicioSeguent[0], posicioSeguent[1])
        elif taula[posicioSeguent[0], posicioSeguent[1]] == '#':
            break
    return



def girarDireccio(turn):
    global direccio

    if turn == 'R':
        direccio = (direccio + 1) % 4
    if turn == 'L':
        direccio = (direccio - 1) % 4
    return

# direccio Right -> 0
# direccio Down -> 1
# direccio Left -> 2
# direccio Up -> 3
direccio = 0

posicioInicial = trobarInici()
print(posicioInicial)

for element in moviments:
    print('Posicio: ', posicioInicial)
    if str(element).isnumeric():
        if direccio == 0:
            moureDreta(element)
        elif direccio == 1:
            moureBaix(element)
        elif direccio == 2:
            moureEsquerra(element)
        elif direccio == 3:
            moureDalt(element)
    else:
        girarDireccio(element)

finalpassword = (1000 * (posicioInicial[0]+1)) + (4 * (posicioInicial[1]+1)) + direccio

print('What is the final password? ', finalpassword)