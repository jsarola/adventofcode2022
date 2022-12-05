from unittest import result


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class Stack:
 
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]
 
    # Get the current size of the stack
    def getSize(self):
        return self.size
 
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
 
    # Get the top item of the stack
    def peek(self):
 
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

fitxer = open('input.txt', 'r')

files = fitxer.readlines()

##     [P]                 [C] [C]    
##     [W]         [B]     [G] [V] [V]
##     [V]         [T] [Z] [J] [T] [S]
##     [D] [L]     [Q] [F] [Z] [W] [R]
##     [C] [N] [R] [H] [L] [Q] [F] [G]
## [F] [M] [Z] [H] [G] [W] [L] [R] [H]
## [R] [H] [M] [C] [P] [C] [V] [N] [W]
## [W] [T] [P] [J] [C] [G] [W] [P] [J]
##  1   2   3   4   5   6   7   8   9 

def crear_pila():
    subpila = Stack()
    subpila.push('W'); subpila.push('R'); subpila.push('F')
    pila.append(subpila)

    subpila = Stack()
    subpila.push('T'); subpila.push('H'); subpila.push('M'); subpila.push('C'); subpila.push('D'); subpila.push('V'); subpila.push('W'); subpila.push('P')
    pila.append(subpila)

    subpila = Stack()
    subpila.push('P'); subpila.push('M'); subpila.push('Z'); subpila.push('N'); subpila.push('L')
    pila.append(subpila)

    subpila = Stack()
    subpila.push('J'); subpila.push('C'); subpila.push('H'); subpila.push('R');
    pila.append(subpila)

    subpila = Stack()
    subpila.push('C'); subpila.push('P'); subpila.push('G'); subpila.push('H'); subpila.push('Q'); subpila.push('T'); subpila.push('B')
    pila.append(subpila)

    subpila = Stack()
    subpila.push('G'); subpila.push('C'); subpila.push('W'); subpila.push('L'); subpila.push('F'); subpila.push('Z')
    pila.append(subpila)

    subpila = Stack()
    subpila.push('W'); subpila.push('V'); subpila.push('L'); subpila.push('Q'); subpila.push('Z'); subpila.push('J'); subpila.push('G'); subpila.push('C')
    pila.append(subpila)

    subpila = Stack()
    subpila.push('P'); subpila.push('N'); subpila.push('R'); subpila.push('F'); subpila.push('W'); subpila.push('T'); subpila.push('V'); subpila.push('C')
    pila.append(subpila)

    subpila = Stack()
    subpila.push('J'); subpila.push('W'); subpila.push('H'); subpila.push('G'); subpila.push('R'); subpila.push('S'); subpila.push('V')
    pila.append(subpila)

pila = []
crear_pila()

for index,lapila in enumerate(pila, start=1):
    print('Initial stack ', index, ':', lapila.getSize())

# CrateMover 9000
resultat_1 = ""

print('CrateMover 9000')
for linea in files:
    # move 2 from 4 to 9
    cadena = linea.split()
    moviments = int(cadena[1])
    pila_inici = int(cadena[3])
    pila_final = int(cadena[5])
    # print(moviments, '-', pila_inici, '-', pila_final)
    for i in range(1, moviments + 1):
        valor = pila[pila_inici-1].pop()
        pila[pila_final-1].push(valor)

for index,lapila in enumerate(pila, start=1):
    print('Final stack ', index, ':', lapila.getSize())

for lapila in pila:
    resultat_1 = resultat_1 + lapila.peek()

print('CrateMover 9000: After the rearrangement procedure completes, what crate ends up on top of each stack? ', resultat_1)

# CrateMover 9001
resultat_2 = ""

pila = []
crear_pila()

print('CrateMover 9001')
for linea in files:
    # move 2 from 4 to 9
    cadena = linea.split()
    moviments = int(cadena[1])
    pila_inici = int(cadena[3])
    pila_final = int(cadena[5])
    # print(moviments, '-', pila_inici, '-', pila_final)
    mover = []
    for i in range(1, moviments + 1):
        mover.append(pila[pila_inici-1].pop())
    for i in reversed(mover):
        pila[pila_final-1].push(i)

for index,lapila in enumerate(pila, start=1):
    print('Final stack ', index, ':', lapila.getSize())

for lapila in pila:
    resultat_2 = resultat_2 + lapila.peek()

print('CrateMover 9001: After the rearrangement procedure completes, what crate ends up on top of each stack? ', resultat_2)

