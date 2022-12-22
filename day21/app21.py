file = 'input.txt'
logging = True

fitxer = open(file, 'r')
files = fitxer.readlines()

class Mico(object):
    def __init__(self, name):
        self.name = name
        self.valor = 0
        self.esquerra = ''
        self.dreta = ''
        self.operacio = ''
        self.pare = ''

llistaMicos = {}

for indexFila, linea in enumerate(files):
    cadena1 = linea.split(':')
    nom = cadena1[0]
    mico = Mico(nom)

    cadena2 = cadena1[1][:-1].strip()
    if cadena2.isnumeric():
        valor = int(cadena2)
        mico.valor = valor
        if nom in llistaMicos:
            llistaMicos[nom].valor = valor
        else:
            llistaMicos[nom] = mico

    else:
        esquerra = cadena2[0:4]
        operacio = cadena2[5]
        dreta = cadena2[7:11]
        mico.operacio = operacio
        mico.esquerra = esquerra
        mico.dreta = dreta
        if mico.esquerra in llistaMicos:
            llistaMicos[mico.esquerra].pare = nom
        else:
            micoNou = Mico(mico.esquerra)
            micoNou.pare = nom
            llistaMicos[mico.esquerra] = micoNou
        if mico.dreta in llistaMicos:
            llistaMicos[mico.dreta].pare = nom
        else:            
            micoNou = Mico(mico.dreta)
            micoNou.pare = nom
            llistaMicos[mico.dreta] = micoNou
        
        if nom in llistaMicos:
            llistaMicos[nom].operacio = operacio
            llistaMicos[nom].esquerra = esquerra
            llistaMicos[nom].dreta = dreta
        else:
            llistaMicos[nom] = mico

#for un in llistaMicos:
#    print(vars(llistaMicos[un]))

def buscarMico(elmico):
    if llistaMicos[elmico].valor > 0:
        solucio = llistaMicos[elmico].valor
    else:
        solucioEsquerra = buscarMico(llistaMicos[elmico].esquerra) 
        solucioDreta = buscarMico(llistaMicos[elmico].dreta)
        operacio = llistaMicos[elmico].operacio
        if operacio == '+':
            solucio = solucioEsquerra + solucioDreta
        elif operacio == '-':
            solucio = solucioEsquerra - solucioDreta
        elif operacio == '*':
            solucio = solucioEsquerra * solucioDreta
        elif operacio == '/':
            solucio = solucioEsquerra / solucioDreta
    
    return solucio

laSolucio = buscarMico('root')

print('What number will the monkey named root yell? ', laSolucio)

def buscarMicoHuman(elmico):
    if elmico == 'humn':
        return 'humn'
    if llistaMicos[elmico].valor > 0:
        solucio = llistaMicos[elmico].valor
    else:
        solucioEsquerra = buscarMico(llistaMicos[elmico].esquerra) 
        solucioDreta = buscarMico(llistaMicos[elmico].dreta)
        operacio = llistaMicos[elmico].operacio
        if operacio == '+':
            solucio = solucioEsquerra + solucioDreta
        elif operacio == '-':
            solucio = solucioEsquerra - solucioDreta
        elif operacio == '*':
            solucio = solucioEsquerra * solucioDreta
        elif operacio == '/':
            solucio = solucioEsquerra / solucioDreta
    
    return solucio

solucioEsq = buscarMicoHuman(llistaMicos['root'].esquerra)
solucioDre = buscarMicoHuman(llistaMicos['root'].dreta)

from sympy import symbols, solve


def buscarExpressio(elmico, elmicofill, laexpressio):
    global formula
    # print('Pare ', elmico, ' FIll', elmicofill)
    # print('esquerra ', llistaMicos[elmico].esquerra, ' dreta', llistaMicos[elmico].dreta)

    if llistaMicos[elmico].pare == '':
        formula = laexpressio
        return

    if llistaMicos[elmico].esquerra == elmicofill:
        if elmicofill == 'humn':
            tmpExpressio = 'x'
        else:
            tmpExpressio = laexpressio
        # print('busco esquerra')
        laexpressio = '(' + tmpExpressio + llistaMicos[elmico].operacio + str(buscarMico(llistaMicos[elmico].dreta)) + ')'
        # print('la expressio', laexpressio)
        buscarExpressio(llistaMicos[elmico].pare, elmico, laexpressio)
    elif llistaMicos[elmico].dreta == elmicofill:
        if elmicofill == 'humn':
            tmpExpressio = 'x'
        else:
            tmpExpressio = laexpressio
        # print('busco dreta')
        laexpressio = '('+ str(buscarMico(llistaMicos[elmico].esquerra)) + llistaMicos[elmico].operacio + tmpExpressio + ')'
        #print('la expressio', laexpressio)
        buscarExpressio(llistaMicos[elmico].pare, elmico, laexpressio)

    # tmpExpressio = buscarExpressio(llistaMicos[elmico].pare, elmico, laexpressio)
    # print('la expressio final', formula)
    return

if solucioEsq == 'humn':
    buscarExpressio(llistaMicos['humn'].pare, 'humn', '')
    print('A')
    expr = str(int(solucioEsq)) + '-' + formula
else:
    buscarExpressio(llistaMicos['humn'].pare, 'humn', '')
    print('B')
    expr = str(int(solucioDre)) + '-' + formula

print('la formula', expr)
x = symbols('x')
# expr = 150-(4+(2*(x-3)))

laSolucio = solve(expr)


print("What number do you yell to pass root's equality test?", laSolucio)

