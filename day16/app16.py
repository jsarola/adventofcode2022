file = 'test.txt'
#file = 'input.txt'
logging = True

fitxer = open(file, 'r')
files = fitxer.readlines()

class Vertex:
    def __init__(self, node, weight):
        self.id = node
        self.weight = weight
        self.adjacent = []

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor):
        self.adjacent.append(neighbor)

    def add_weight(self, weight):
        self.weight = weight

    def get_id(self):
        return self.id

    def get_connections(self):
        return self.adjacent # list

    def get_weight(self):
        return self.weight

class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, node, weight = 0):
        self.num_vertices = self.num_vertices + 1
        if node not in self.vertices:
            new_vertex = Vertex(node, weight)
            self.vertices[node] = new_vertex
        else:
            new_vertex = self.get_vertex(node)
            new_vertex.add_weight(weight)
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, fromEdge, toEdge):
        if toEdge not in self.vertices:
            self.add_vertex(toEdge)
        self.get_vertex(fromEdge).add_neighbor(toEdge)

laCova = Graph()

# Valve II has flow rate=0; tunnels lead to valves AA, JJ
for indexFila, linea in enumerate(files):
    # if logging: print('Fila ', indexFila)
    cadena = linea.split()

    novaValvula = cadena[1].strip()
    nouVertex = laCova.add_vertex(novaValvula)

    ratetmp = cadena[4][:-1]
    ratetmp2 = ratetmp.split('=')
    fluxValvula = int(ratetmp2[1])
    if 'valves' in linea:
        valvulestmp = linea[:-1].split('valves')
    else:
        valvulestmp = linea[:-1].split('valve')
    if ',' in valvulestmp[1]:
        valvulestmp2 = valvulestmp[1].split(',')
    else:
        valvulestmp2 = [valvulestmp[1]]
    
    for valvula in valvulestmp2:
        nouVertex.add_weight(fluxValvula)
        laCova.add_edge(novaValvula, valvula.strip())

def buscarValvula(vertex):
    pesTrobat = 0

    for x in vertex.get_connections():
        vertexTmp = laCova.get_vertex(x)
        if x in valvulesOpen:
            if vertexTmp.get_weight() > pesTrobat:
                pesTrobat = vertexTmp.get_weight()
                valvulaTornar = x

    return valvulaTornar



#for vertexs in laCova:
#    print('ID ', vertexs.id, ' WEIGHT: ', vertexs.weight, 'Neighbours: ', vertexs.adjacent)

laPressio = 0

minute = 0
maxMinutes = 30
valvulesOpen = []
flowRate = 0

vertexBuscar = laCova.get_vertex('AA')

while minute < maxMinutes:
    if logging: print('Minut: ', minute, '->', vertexBuscar.id)
    vertexTmp = buscarValvula(vertexBuscar)
    if vertexTmp in valvulesOpen:
        minute = minute + 1        
    else:
        minute = minute + 2
        flowRate = flowRate + (maxMinutes - minute) * laCova.get_vertex(vertexTmp).weight
        valvulesOpen.append(vertexTmp)
    vertexBuscar = laCova.get_vertex(vertexTmp)

print('Flow released ', flowRate)
print('Llista valvules ', valvulesOpen)

print('What is the most pressure you can release? ', laPressio)