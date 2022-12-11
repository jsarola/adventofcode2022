import math

file = 'input.txt'
logging = False

elsmicos = []
elsmicos2 = []

def imprimirLog(text):
    if logging == True:
        print(text)

def obtenirMicos():
    micos = []
    fitxer = open('input.txt', 'r')
    files = fitxer.readlines()

    for quinaLinea, linea in enumerate(files):
        cadena = linea[:-1].split()
        if len(cadena) > 0:
            task = cadena[0].strip()
        else:
            task = ''
            micos.append([elsitems, operation, operationValue, divisibleby, throwifistrue, throwifisfalse,0])
        if task == 'Monkey':
            tmp = cadena[1]
            mico = int(tmp[:-1])
        elif task == 'Starting':
            tmp = linea[:-1].split(':')
            tmp2 = tmp[1].split(',')
            elsitems = []
            for item in tmp2:
                elsitems.append(float(item))
        elif task == 'Operation:':
            tmp = linea[:-1].split(':')
            tmp2 = tmp[1].split('=')
            tmp3 = tmp2[1].split()
            operation = tmp3[1]
            operationValue = tmp3[2]
        elif task == 'Test:':
            tmp = linea[:-1].split(':')
            tmp2 = tmp[1].split('by')
            divisibleby = int(tmp2[1])
        elif task == 'If':
            escert = cadena[1]
            if escert == 'true:':
                throwifistrue = int(cadena[5])
            else:
                throwifisfalse = int(cadena[5])
        elif task == 'Stop':
            break
    return micos

elsmicos = obtenirMicos()

modulus = 1
for item in elsmicos:
    if logging: print('Mico: ', item)
    modulus = modulus * item[3]

max_round = 20

for ronda in range(1,max_round+1):
    if logging: print('Round: ', ronda)
    for quinMico, mico in enumerate(elsmicos):
        if logging: print('Round: ', ronda, 'Mico: ', quinMico)
        for item in mico[0]:
            if logging: print('Round: ', ronda, 'Mico: ', quinMico, 'Item:', item)
            if mico[2] == 'old':
                worryIncrease = item
            else:
                worryIncrease = float(mico[2])
            
            if mico[1] == '+':
                worry = item + worryIncrease
            elif mico[1] == '*':
                worry = item * worryIncrease
            else:
                pass

            tmp = worry / 3
            newWorry = math.floor(tmp)

            if newWorry % mico[3] == 0:
                elsmicos[mico[4]][0].append(float(newWorry))
            else:
                elsmicos[mico[5]][0].append(float(newWorry))
        mico[6] = mico[6] + len(mico[0])
        mico[0] = []
    if ronda % 100:
        for item in elsmicos:
            if logging: print('Mico: ', item)

llista_inspected = []
for item in elsmicos:
    llista_inspected.append(item[6])
if logging: print('Llista inspected: ', llista_inspected)
llista_inspected_sort = sorted(llista_inspected, reverse=True)
producte = llista_inspected_sort[0] * llista_inspected_sort[1]
print('What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?:', producte)

# Part two
max_round = 10000

elsmicos2 = obtenirMicos()

for ronda in range(1,max_round+1):
    if logging: print('Round: ', ronda)
    for quinMico, mico in enumerate(elsmicos2):
        if logging: print('Round: ', ronda, 'Mico: ', quinMico)
        for item in mico[0]:
            if logging: print('Round: ', ronda, 'Mico: ', quinMico, 'Item:', item)
            if mico[2] == 'old':
                worryIncrease = item
            else:
                worryIncrease = float(mico[2])
            
            if mico[1] == '+':
                worry = item + worryIncrease
            elif mico[1] == '*':
                worry = item * worryIncrease
            else:
                pass

            tmp = worry % modulus
            newWorry = math.floor(tmp)

            if newWorry % mico[3] == 0:
                elsmicos2[mico[4]][0].append(float(newWorry))
            else:
                elsmicos2[mico[5]][0].append(float(newWorry))
        mico[6] = mico[6] + len(mico[0])
        mico[0] = []
    if ronda % 1000:
        for item in elsmicos2:
            if logging: print('Mico: ', item)

llista_inspected = []

for item in elsmicos2:
    llista_inspected.append(item[6])
if logging: print('Llista inspected: ', llista_inspected)
llista_inspected_sort = sorted(llista_inspected, reverse=True)
producte = llista_inspected_sort[0] * llista_inspected_sort[1]

print('what is the level of monkey business after 10000 rounds?:', producte)