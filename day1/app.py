fitxer = open('input.txt', 'r')

files = fitxer.readlines()

count = 0
increased = 0

suma_gran = 0
suma_actual = 0

llista_elf = []

for fila in files:
    try:
        fila_actual = int(fila)
    except:
        fila_actual = 0
    
    print(fila_actual)
    if fila_actual == 0:
        if suma_actual > suma_gran:
            suma_gran = suma_actual
        llista_elf.append(suma_actual)
        suma_actual = 0
    else:
        suma_actual = suma_actual + fila_actual

print("Part1 -> How many total Calories is that Elf carrying?: ", suma_gran)

llista_elf_sorted = sorted(llista_elf)

suma_3_elfs = llista_elf_sorted[-1] + llista_elf_sorted[-2] + llista_elf_sorted[-3]

print(llista_elf_sorted)

print("Part1 -> How many Calories are those Elves carrying in total?: ", suma_3_elfs)