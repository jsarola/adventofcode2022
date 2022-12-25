file = 'input.txt'
logging = False

fitxer = open(file, 'r')
files = fitxer.readlines()

totalLlista = 0

for indexFila, linea in enumerate(files):
    llarg = len(linea[:-1])
    total = 0
    # get the values
    valors = [a for a in linea[:-1]]
    # reversed
    valorsReversed = list(reversed(valors))


    for pos, caracter in enumerate(valorsReversed):
        if caracter.isnumeric():
            valor = int(caracter)
        elif caracter == '-':
            valor = -1
        elif caracter == '=':
            valor = -2
        total = total + valor * (5 ** pos)

    totalLlista = totalLlista + total

llistaSolucio = []

def buscarIndex(valor):
    index = 0
    while valor > 2 * (5**index):
        index = index + 1

    return index

def buscarSolucio(valor, index):
    global llistaSolucio
    if logging: print('INICI ', valor, index)
    if index < 0:
        if valor != 0:
            return False
        else:
            return True

    for pos in (2,1,0,-1,-2):
        # print('POS: ', pos, llistaSolucio)
        resta = pos * (5 ** index)
        if abs(valor - resta) <= (5 ** index):
            llistaSolucio.append(pos)
            if buscarSolucio(valor - resta, index - 1):
                return True
            else:
                llistaSolucio.pop()

    return False

indexPrimer = buscarIndex(totalLlista)

buscarSolucio(totalLlista,indexPrimer)

laSolucio = ''

for pos, caracter in enumerate(llistaSolucio):
    if caracter >= 0:
        laSolucio = laSolucio + str(caracter)
    elif caracter == -1:
        laSolucio = laSolucio + '-'
    elif caracter == -2:
        laSolucio = laSolucio + '='

print(' What SNAFU number do you supply to Bob\'s console? ', laSolucio)
