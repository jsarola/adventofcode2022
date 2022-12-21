file = 'test.txt'
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

def buscarExpressio(elmico, laexpressio):
    print('laexpressio', laexpressio)
    if llistaMicos[elmico].esquerra == 'humn':
        laexpressio = buscarExpressio(llistaMicos[elmico].pare, '(x' + llistaMicos[elmico].operacio + str(buscarMico(llistaMicos[elmico].dreta)) + ')')
    elif llistaMicos[elmico].dreta == 'humn':
        laexpressio = buscarExpressio(llistaMicos[elmico].pare, '('+ str(buscarMico(llistaMicos[elmico].esquerra)) + llistaMicos[elmico].operacio + 'x)')
    else:
        laexpressio = ''   
    return laexpressio

if solucioEsq == 'humn':
    print('A')
    formula = buscarExpressio(llistaMicos['humn'].pare, '')
    expr = str(int(solucioDre)) + '-' + formula
else:
    print('B')
    formula = buscarExpressio(llistaMicos['humn'].pare, '')
    expr = str(int(solucioEsq)) + '-' + formula

print('la formula', expr)
x = symbols('x')
# expr = 150-(x-10)

# laSolucio = solve(expr)


print("What number do you yell to pass root's equality test?", laSolucio)

