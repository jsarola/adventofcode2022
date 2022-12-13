import json

file = 'input.txt'
logging = True

fitxer = open(file, 'r')
files = fitxer.readlines()

cadena = []
cadena0 = []
cadena1 = []
pos = 0
grup = 0
totalIndex = 0

def compararEnter(leftEnter, rightEnter):
    # if logging: print('Number -> Left: ', leftEnter, ' - Right: ', rightEnter )
    if leftEnter == rightEnter:
        return 'Igual'
    elif leftEnter < rightEnter:
        return 'Petit'
    else:
        return 'Gran'

def compararList(left, right):
    # if logging: print('List -> Left: ', left, ' - Right: ', right )
    rightOrder = False
    retorn = 'NoIgual'
    if len(left) == 0 and len(right) == 0:
        # if logging: print('Dos buides')
        return 'Igual'
    elif len(left) == 0:
        # if logging: print('Esquerra és buida')
        return 'Petit'
    elif len(right) == 0:
        # if logging: print('Dreta és buida')
        return 'Gran'

    for i in range(0, len(left)):
        try:
            x = right[i]
        except:
            return 'Gran'
        # if logging: print('For list ', i, ' -> Left: ', left[i], ' - Right: ', right[i] )
        if isinstance(left[i], list) and isinstance(right[i], list):            
            # if logging: print('Les dos son llistes')
            comparacio = compararList(left[i], right[i])
            if comparacio == 'Petit':
                rightOrder = 'Petit'
                break
            elif comparacio == 'Igual':
                retorn = 'Igual'
            elif comparacio == 'Gran':
                retorn = 'NoIgual'
                rightOrder = 'Gran'
                break
        elif isinstance(left[i], list):
            # if logging: print('Esquerra és llista')
            comparacio = compararList(left[i],[right[i]])
            if comparacio == 'Petit':
                rightOrder = 'Petit'
                break
            elif comparacio == 'Igual':
                retorn = 'Igual'
            elif comparacio == 'Gran':
                retorn = 'NoIgual'
                rightOrder = 'Gran'
                break
        elif isinstance(right[i], list):
            # if logging: print('Dreta és llista')
            comparacio = compararList([left[i]],right[i])
            if comparacio == 'Petit':
                rightOrder = 'Petit'
                break
            elif comparacio == 'Igual':
                retorn = 'Igual'
            elif comparacio == 'Gran':
                retorn = 'NoIgual'
                rightOrder = 'Gran'
                break
        else:
            # if logging: print('Comparar numeros', i)
            esquerra = left[i]
            dreta = right[i]
            comparacio = compararEnter(esquerra, dreta)
            if comparacio == 'Petit':
                retorn = 'NoIgual'
                rightOrder = 'Petit'
                break
            elif comparacio == 'Igual':
                retorn = 'Igual'
            elif comparacio ==  'Gran':
                retorn = 'NoIgual'
                rightOrder = 'Gran'
                break
    if retorn == 'Igual':
        rightOrder = 'Igual'
    return rightOrder

for indexFila, linea in enumerate(files):
    if linea == '\n':
        grup = grup + 1        
        cadena1 = json.loads(cadena[0])
        cadena2 = json.loads(cadena[1])
        cadena = []
        pos = 0
        comparacio = compararList(cadena1, cadena2)
        if comparacio == 'Petit' or comparacio == 'Igual':
            # if logging: print('isRighOrder: ', grup)
            totalIndex = totalIndex + grup
    else:        
        cadena.append(linea[:-1])
        pos = pos + 1
        
print('What is the sum of the indices of those pairs? ', totalIndex)

cadena = []
for indexFila, linea in enumerate(files):
    if linea == '\n':
        continue
    else:
        cadenatmp = linea[:-1]
        cadena.append(json.loads(cadenatmp))

divider1 = [[2]]
divider2 = [[6]]
cadena.append(divider1)
cadena.append(divider2)

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element            
            comparacio = compararList(arr[j], arr[j + 1])
            if comparacio == 'Gran':
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

bubbleSort(cadena)

for index, item in enumerate(cadena):
    # if logging: print(index, '->', item)
    if item == divider1:        
        divider1index = index + 1
    if item == divider2:
        divider2index = index + 1

decoderKey = divider1index * divider2index
print('What is the decoder key for the distress signal? ', decoderKey)