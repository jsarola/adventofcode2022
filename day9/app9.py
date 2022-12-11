fitxer = open('input.txt', 'r')

files = fitxer.readlines()

taula = []

posH = [0, 0]
posT = [0, 0]

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

taulaOcupats = []

taulaOcupats.append(posT)

for quinaLinea, linea in enumerate(files):
    cadena = linea[:-1].split()
    moviment = cadena[0]
    posicions = int(cadena[1])
    
    if moviment == 'R':
        for i in range(1,posicions+1):
            posH = [posH[0], posH[1]+1]
            if not adjunts(posH, posT):
                if posH[0] == posT[0]:
                    posT = [posT[0], posT[1]+1]
                elif posH[0] > posT[0]:
                    posT = [posT[0]+1, posT[1]+1]
                else:
                    posT = [posT[0]-1, posT[1]+1]
                if posT not in taulaOcupats:
                    taulaOcupats.append(posT)
    if moviment == 'U':
        for i in range(1,posicions+1):
            posH = [posH[0]+1, posH[1]]
            if not adjunts(posH, posT):
                if posH[1] == posT[1]:
                    posT = [posT[0]+1, posT[1]]
                elif posH[1] > posT[1]:
                    posT = [posT[0]+1, posT[1]+1]
                else:
                    posT = [posT[0]+1, posT[1]-1]
                if posT not in taulaOcupats:
                    taulaOcupats.append(posT)
    if moviment == 'L':
        for i in range(1,posicions+1):
            posH = [posH[0], posH[1]-1]
            if not adjunts(posH, posT):
                if posH[0] == posT[0]:
                    posT = [posT[0], posT[1]-1]
                elif posH[0] > posT[0]:
                    posT = [posT[0]+1, posT[1]-1]
                else:
                    posT = [posT[0]-1, posT[1]-1]
                if posT not in taulaOcupats:
                    taulaOcupats.append(posT)
    if moviment == 'D':
        for i in range(1,posicions+1):
            posH = [posH[0]-1, posH[1]]            
            if not adjunts(posH, posT):
                if posH[1] == posT[1]:
                    posT = [posT[0]-1, posT[1]]
                elif posH[1] > posT[1]:
                    posT = [posT[0]-1, posT[1]+1]
                else:
                    posT = [posT[0]-1, posT[1]-1]
                if posT not in taulaOcupats:
                    taulaOcupats.append(posT)
    
    # print('Linea: ', quinaLinea+1, '(', posH, ',', posT, ')' )
    if moviment == 'STOP':
        break

print('Part one: How many positions does the tail of the rope visit at least once?', len(taulaOcupats))

# part two

rope = []
number_knots = 9

for i in range(0,number_knots + 1):
    rope.append([0, 0])

taulaOcupats2 = []

# first place
taulaOcupats2.append([0, 0])

def moureCua(H,T):
    head = H
    tail = T
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            tail[1] = tail[1] + 1
        else:
            tail[1] = tail[1] - 1
        return tail
    
    if head[1] == tail[1]:
        if head[0] > tail[0]:
            tail[0] = tail[0] + 1
        else:
            tail[0] = tail[0] - 1
        return tail

    if head[0] > tail[0]:
        if head[1] > tail[1]:
            tail[0] = tail[0] + 1
            tail[1] = tail[1] + 1
        else:
            tail[0] = tail[0] + 1
            tail[1] = tail[1] - 1
    else:
        if head[1] > tail[1]:
            tail[0] = tail[0] - 1
            tail[1] = tail[1] + 1
        else:
            tail[0] = tail[0] - 1
            tail[1] = tail[1] - 1
    return tail

for quinaLinea, linea in enumerate(files):
    cadena = linea[:-1].split()
    moviment = cadena[0]
    posicions = int(cadena[1])
    
    if moviment == 'R':
        for i in range(1,posicions+1):
            posH = rope[0]
            posH = [posH[0], posH[1]+1]
            rope[0] = posH
            for element in range(0,number_knots):
                posH = rope[element]
                posT = rope[element+1]
                if not adjunts(posH, posT):
                    posT = moureCua(posH, posT)
                    rope[element+1] = posT
            lastElement = rope[9]
            # print('before last element: ', lastElement, '->', taulaOcupats2)
            if lastElement not in taulaOcupats2:
                taulaOcupats2.append([lastElement[0], lastElement[1]])

    if moviment == 'U':
        for i in range(1,posicions+1):
            posH = rope[0]
            posH = [posH[0]+1, posH[1]]
            rope[0] = posH
            for element in range(0,number_knots):
                posH = rope[element]
                posT = rope[element+1]
                if not adjunts(posH, posT):
                    posT = moureCua(posH, posT)
                    rope[element+1] = posT
            lastElement = rope[9]
            # print('last element: ', lastElement, '->', taulaOcupats2)
            if lastElement not in taulaOcupats2:
                taulaOcupats2.append([lastElement[0], lastElement[1]])

    if moviment == 'L':
        for i in range(1,posicions+1):
            posH = rope[0]
            posH = [posH[0], posH[1]-1]
            rope[0] = posH
            for element in range(0,number_knots):
                posH = rope[element]
                posT = rope[element+1]
                if not adjunts(posH, posT):
                    posT = moureCua(posH, posT)
                    rope[element+1] = posT
            lastElement = rope[9]
            # print('last element: ', lastElement, '->', taulaOcupats2)
            if lastElement not in taulaOcupats2:
                taulaOcupats2.append([lastElement[0], lastElement[1]])
    
    if moviment == 'D':
        for i in range(1,posicions+1):
            posH = rope[0]
            posH = [posH[0]-1, posH[1]]
            rope[0] = posH
            for element in range(0,number_knots):
                posH = rope[element]
                posT = rope[element+1]
                if not adjunts(posH, posT):
                    posT = moureCua(posH, posT)
                    rope[element+1] = posT
            lastElement = rope[9]
            # print('last element: ', lastElement, '->', taulaOcupats2)
            if lastElement not in taulaOcupats2:
                taulaOcupats2.append([lastElement[0], lastElement[1]])
    
    # print('taula', taulaOcupats2)

print('Part two: How many positions does the tail of the rope visit at least once?', len(taulaOcupats2))