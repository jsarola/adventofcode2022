file = 'test.txt'
logging = True

fitxer = open(file, 'r')
files = fitxer.readlines()

llista = []

for index, linea in enumerate(files):
    llista.append([index, int(linea[:-1])])
    if int(linea[:-1]) == 0:
        numero0 = [index, 0]

llargLlista = len(llista)
if logging: print('LLista: ', llista, ' Llarg: ', llargLlista)

llistaOriginal = llista.copy()

for index, numero in enumerate(llistaOriginal):
    posicio = llista.index(numero)
    
    if numero[1] != 0:
        llista.remove(numero)
        if numero[1] < 0:
            posicioa = (posicio + numero[1]) % llargLlista
            posiciob = (posicio + numero[1] - 1) % llargLlista
            print(numero[1], '-', posicioa, posiciob)
        else:
            posicioa = (posicio + numero[1]) % llargLlista
            posiciob = (posicio + numero[1] + 1) % llargLlista
            print(numero[1], '-', posicioa, posiciob)
    
        if (posicio + numero[1]) > llargLlista:
            novaPosicio = (posicio + numero[1] + 1) % llargLlista
        elif posicio + numero[1] <= 0:
            novaPosicio = (posicio + numero[1] - 1) % llargLlista
        else:
            novaPosicio = (posicio + numero[1]) % llargLlista
        if logging: print(llista)
        llista.insert(novaPosicio, numero)

  
    #if logging: print('Pas ', index + 1, posicio, '-', novaPosicio, ' : ', llista)

if logging: print('LLista final: ', llista)

posicio0 = llista.index(numero0)

valor1000 = llista[(posicio0 + 1000) % (llargLlista)]
valor2000 = llista[(posicio0 + 2000) % (llargLlista)]
valor3000 = llista[(posicio0 + 3000) % (llargLlista)]

if logging: print(valor1000, valor2000, valor3000)

print('What is the sum of the three numbers that form the grove coordinates? ', valor1000[1]+valor2000[1]+valor3000[1])