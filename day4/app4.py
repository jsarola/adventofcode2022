fitxer = open('input.txt', 'r')

files = fitxer.readlines()

suma_1 = 0
suma_2 = 0

linia_fitxer = 1

for fila in files:
    fila = fila[:-1]
    cadena = fila.split(',')
    elf1 = cadena[0]
    elf2 = cadena[1]
    # print(elf1, '-', elf2)
    elf1 = elf1.split('-')
    elf2 = elf2.split('-')
    # print(elf1, '-', elf2)
    cadena_elf1 = []
    cadena_elf2 = []
    for i in range(int(elf1[0]),int(elf1[1])+1):
        cadena_elf1.append(i)
    for i in range(int(elf2[0]),int(elf2[1])+1):
        cadena_elf2.append(i)
    # print(cadena_elf1, '-', cadena_elf2)

    # part 1 (all)
    if all(x in cadena_elf2 for x in cadena_elf1):
        suma_1 = suma_1 + 1
        # print('elf1 in elf2 (', linia_fitxer, '): ', cadena_elf1, '-', cadena_elf2)
    elif all(x in cadena_elf1 for x in cadena_elf2):
        suma_1 = suma_1 + 1
        # print('elf2 in elf1 (', linia_fitxer, '): ', cadena_elf1, '-', cadena_elf2)
    else: 
        pass
        # print('elf1 not in elf2 (', linia_fitxer, '): ', cadena_elf1, '-', cadena_elf2)

    # part 2 (any)
    if any(x in cadena_elf2 for x in cadena_elf1):
        suma_2 = suma_2 + 1
        # print(elf1, '-', elf2)
        # print('elf1 some in elf2 (', linia_fitxer, '): ', cadena_elf1, '-', cadena_elf2)
    else:        
        pass
        # print('elf1 not in elf2 (', linia_fitxer, '): ', cadena_elf1, '-', cadena_elf2)

    linia_fitxer = linia_fitxer + 1 

print('In how many assignment pairs does one range fully contain the other? ', suma_1)

print('In how many assignment pairs do the ranges overlap? ', suma_2)