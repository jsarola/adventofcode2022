from treelib import Node, Tree

class Tamany(object):
    def __init__(self, mida, carpeta):
        self.mida = mida
        self.carpeta = carpeta

def canviarMida(identificador, sizeCarpeta):
    tagCarpeta = arbre.get_node(identificador).tag
    midaCarpeta = arbre.get_node(identificador).data.mida
    midaCarpeta = midaCarpeta + int(sizeCarpeta)
    # print('Carpeta: ', tagCarpeta, '->', midaCarpeta)
    arbre.update_node(identificador, data=Tamany(midaCarpeta, True))

    papa = arbre.parent(identificador)
    if papa is None:
        return 1
    else:        
        return canviarMida(papa.identifier, sizeCarpeta)

fitxer = open('input.txt', 'r')

files = fitxer.readlines()

arbre = Tree()

arbre.create_node("/", data=Tamany(0, True))

pare = arbre.root
suma_pare = 0
suma_fill = 0

for linea in files:
    cadena = linea.split()
    if cadena[0] == "$":
        if cadena[1] == "cd":            
            if cadena[2] == "/":
                # arbre.crea_node("/", "/")
                # pare = "/"
                continue
            elif cadena[2] == "..":
                # pare = ""                
                pare = arbre.parent(fill.identifier)
                fill = pare
                suma_fill = 0
                # print('Pare: ', pare.identifier)
            else:                
                fill = arbre.create_node(cadena[2], parent=pare, data=Tamany(0, True))
                pare = fill.identifier
                suma_fill = 0
                # print('Fill: ', fill.identifier)
    elif cadena[0] == "dir":
        continue
    elif cadena[0] == "STOP":
        break
    else:
        tamany = cadena[0]
        arbre.create_node(cadena[1], parent=pare, data=Tamany(tamany, False))
        canviarMida(pare, int(tamany))

arbre.show(data_property="mida")

suma_total = 0
for node in  arbre.all_nodes_itr():
    if node.data.carpeta:
        # print(node.tag, node.data.mida)
        if int(node.data.mida) < 100000:
            suma_total = suma_total + int(node.data.mida)

print('What is the sum of the total sizes of those directories? ', suma_total)

sizeTotal = int(arbre.get_node(arbre.root).data.mida)

sizeTrobat = 70000000 - sizeTotal

print('the size of the unused space must currently be ', sizeTrobat)

sizeBuscar = 30000000 - sizeTrobat

print('the update still require at least ', sizeBuscar)

llista = []
for node in  arbre.all_nodes_itr():
    if node.data.carpeta:
        if int(node.data.mida) > sizeBuscar:
            print(node.tag, node.data.mida)
            llista.append(int(node.data.mida))

llistaSorted = sorted(llista)

print('What is the total size of that directory? ', llistaSorted[0])

