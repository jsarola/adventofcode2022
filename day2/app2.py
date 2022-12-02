fitxer = open('input.txt', 'r')

files = fitxer.readlines()

suma = 0
suma_2 = 0


for fila in files:
    operacio = 0

    cadena = fila.split()
    opponent = cadena[0]
    mine = cadena[1]

    # print(opponent, " -> ", mine)

    if mine == 'X':
        operacio = 1
        if opponent == 'A':
            operacio = operacio + 3
        if opponent == 'C':
            operacio = operacio + 6
    if mine == 'Y':
        operacio = 2
        if opponent == 'A':
            operacio = operacio + 6
        if opponent == 'B':
            operacio = operacio + 3
    if mine == 'Z':
        operacio = 3
        if opponent == 'B':
            operacio = operacio + 6
        if opponent == 'C':
            operacio = operacio + 3

    suma = suma + operacio

print("Part1 -> What would your total score be if everything goes exactly according to your strategy guide??: ", suma)

for fila in files:
    operacio = 0

    cadena = fila.split()
    opponent = cadena[0]
    mine = cadena[1]

    # print(opponent, " -> ", mine)

    if mine == 'X':
        operacio = 0
        if opponent == 'A':
            operacio = operacio + 3
        if opponent == 'B':
            operacio = operacio + 1
        if opponent == 'C':
            operacio = operacio + 2
    if mine == 'Y':
        operacio = 3
        if opponent == 'A':
            operacio = operacio + 1
        if opponent == 'B':
            operacio = operacio + 2
        if opponent == 'C':
            operacio = operacio + 3
    if mine == 'Z':
        operacio = 6
        if opponent == 'A':
            operacio = operacio + 2
        if opponent == 'B':
            operacio = operacio + 3
        if opponent == 'C':
            operacio = operacio + 1

    suma_2 = suma_2 + operacio

print("Part2 -> what would your total score be if everything goes exactly according to your strategy guide?: ", suma_2)