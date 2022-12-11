fitxer = open('input.txt', 'r')

files = fitxer.readlines()

cicle = 1
position = 0
valorX = 1
totalSignalStrength = 0

spriteLine = []

for quinaLinea, linea in enumerate(files):
    cadena = linea[:-1].split()
    operation = cadena[0]
    if len(cadena) > 1:
        value = int(cadena[1])
    else:
        value = 0

    if operation == 'noop':
        # print('sprite:', ''.join(spriteLine), ' position:', position, ' cicle:', cicle, ' valorX:', valorX)
        if (position % 40) in (valorX -1, valorX, valorX + 1):
            spriteLine.append('#')
        else:  
            spriteLine.append('.')
        cicle = cicle + 1
        position = position + 1
        if cicle in (20,60,100,140,180,220):
            print('Total:', cicle, '-', valorX)
            signalStrength = cicle * valorX
            totalSignalStrength = totalSignalStrength + signalStrength
    elif operation == 'addx':
        for i in (1,2):            
            # print('sprite:', ''.join(spriteLine), ' position:', position, ' cicle:', cicle, ' valorX:', valorX)
            if (position % 40) in (valorX -1, valorX, valorX + 1):
                spriteLine.append('#')
            else:  
                spriteLine.append('.')
            cicle = cicle + 1
            position = position + 1
            if i == 2:
                valorX = valorX + value
            if cicle in (20,60,100,140,180,220):
                print('Total:', cicle, '-', valorX)
                signalStrength = cicle * valorX
                totalSignalStrength = totalSignalStrength + signalStrength
    elif operation == 'stop':
        break

    # print('Linea: ', quinaLinea+1, '(', operation, ',', value, ')' )

print('What is the sum of these six signal strengths? ', totalSignalStrength)

print(len(spriteLine))

print(''.join(spriteLine[0:40]))
print(''.join(spriteLine[40:80]))
print(''.join(spriteLine[80:120]))
print(''.join(spriteLine[120:160]))
print(''.join(spriteLine[160:200]))
print(''.join(spriteLine[200:240]))