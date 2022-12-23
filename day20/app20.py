file = 'test.txt'
logging = True

fitxer = open(file, 'r')
files = fitxer.readlines()

llista = []

for index, linea in enumerate(files):
    llista.append([index, int(linea[:-1])])

llargLlista = len(llista)
if logging: print('LLista: ', llista, ' Llarg: ', llargLlista)

llistaOriginal = llista.copy()

for index, numero in enumerate(llistaOriginal):
    posicio = llista.index(numero)
    
    novaPosicio = (posicio + numero[1] + 1) % (llargLlista + 1) - 1

    print(posicio, novaPosicio)

    llista.remove(numero)
    llista.insert(novaPosicio, numero)
    
    if logging: print('LLista provisional: ', llista)

if logging: print('LLista final: ', llista)