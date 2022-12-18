

# rock[0] = '-'
# rock[1] = '+'
# rock[2] = 'L' al reves
# rock[3] = '|'
# rock[4] = '#'
# 
# moviments = llista()
# max_moviments = len(moviments)
# 
# per rock de 0 a 2022
#   posicio_inicial_rock(rock mod 5)
# 
#   mentres no estigui a baix(rock):
#      moure_rock(moviment(index_moviment%max_moviments))
#      moura_rock_avall
#      index_moviment = index_moviment+1


file = 'test.txt'
#file = 'input.txt'
logging = True

fitxer = open(file, 'r')
files = fitxer.readlines()

moviment = []
for indexFila, linea in enumerate(files):
    for caracter in linea[:-1]:
        if caracter == '<':
            moviment.append(0)
        else:
            moviment.append(1)

max_moviment = len(moviment)

max_roques = 2022

roc = [['0'],['1'],['2'],['3'],['4']]
laroca = []
torre = [['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.']]
files = 3

def buscarFilaInicial():
    global files

    ultimaFila = - 1
    for fila in reversed(range(files)):
        if '#' in torre[fila]:
            ultimaFila = fila
            break
    
    for i in range(files, files + ultimaFila):
        torre.append(['.','.','.','.','.','.','.'])

    return files + ultimaFila + 1



def posar_roca(quinaRoca):
    global laroca
    global files

    fila = buscarFilaInicial()
    files = fila - 1
    if quinaRoca == 0:
        laroca = [(fila, 2), (fila, 3), (fila , 4), (fila, 5)]
    elif quinaRoca == 1:
        laroca = [(fila, 3), (fila+1, 2), (fila+1, 3), (fila+1, 4), (fila+2, 3)]
    elif quinaRoca == 2:
        laroca = [(fila, 2), (fila, 3), (fila , 4), (fila+1, 4), (fila+2, 4)]
    elif quinaRoca == 3:
        laroca = [(fila, 2), (fila+1, 2), (fila+2 , 2), (fila+3, 2)]
    elif quinaRoca == 4:
        laroca = [(fila, 2), (fila+1, 2), (fila , 3), (fila+1, 3)]

def moure_roca(quinMoviment):
    global laroca

    novaRoca = []
    if quinMoviment == 0:
        for element in laroca:
            novaColumna = element[1] + 1
            if novaColumna < 0:
                return
            elif element[0] < files:
                if torre[element[0]][novaColumna] == '#':
                    return
                else:
                    novaRoca.append((element[0], novaColumna))
                return
            else:
                novaRoca.append((element[0], novaColumna))
        laroca = novaRoca.copy()
    else:
        for element in laroca:
            novaColumna = element[1] + 1
            if novaColumna > 6:
                return
            elif element[0] < files:
                if torre[element[0]][novaColumna] == '#':
                    return
                else:
                    novaRoca.append((element[0], novaColumna))
            else:
                novaRoca.append((element[0], novaColumna))
        laroca = novaRoca.copy()
    return

def baixar_roca():
    global laroca

    novaRoca = []
    for element in laroca:
        novaFila = element[0] - 1
        novaRoca.append((novaFila,element[1]))
    laroca = novaRoca.copy()

def roca_es_pot_moure():
    for element in laroca:
        novaFila = element[0] - 1
        if novaFila < 0:
            return False
        elif torre[novaFila][element[1]] == '#':
            return False
    return True

for roca in range(0, max_roques):
    posar_roca(roca % 5)

    elmoviment = 0
    while roca_es_pot_moure():
        moure_roca(moviment[elmoviment % max_moviment])
        elmoviment = elmoviment + 1
        baixar_roca()
        print('moviment', elmoviment, laroca)
    
    break

print(torre)