fitxer = open('input.txt', 'r')

files = fitxer.readlines()

# First 4 characters
for cadena in files:
    for index,caracter in enumerate(cadena):
        marca = cadena[index:index+4]
        if all([marca[i] not in marca[:i] + marca[i+1:] for i in range(len(marca))]):
            print(index, '->', marca)
            break

print('First 4 chars: How many characters need to be processed before the first start-of-packet marker is detected? ', index + 4)

# First 14 characters
for cadena in files:
    for index,caracter in enumerate(cadena):
        marca = cadena[index:index+14]
        if all([marca[i] not in marca[:i] + marca[i+1:] for i in range(len(marca))]):
            print(index, '->', marca)
            break

print('First 14 chars: How many characters need to be processed before the first start-of-packet marker is detected? ', index + 14)