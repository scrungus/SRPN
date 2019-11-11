import math as m

def addStack(elem):
    if(len(stack) >= 23):
        print('Stack Overflow')
    else:
        stack.append(elem)
    return

def checkSat(elem):
    if elem > MAX:
        return MAX
    elif elem < -MAX:
        return -MAX
    else:
        return elem

def printStack():
    for i in range(len(stack)):
        print(m.trunc(stack[i]))
    return

""" def findOffender(elem):
    for i in range(len(elem)):
        if not elem[i].isdigit():
            return elem[i] """

def parseInfix(elem):
    print("parsing infix...")


def performOperation(elem):
    #invalid operations
    if not elem in validoperations:
        return       
    #read-only operations
    if elem == 'd':
        printStack()
        return
    if elem == '=':
        print(m.trunc(stack[-1]))
        return
    if elem == 'r':
        return
    #write operations
    if(len(stack)>=2):
        y = float(stack.pop())
        x = float(stack.pop())
    else:
        print('Stack Underflow')
        return

    if elem == '*':
        return checkSat(x*y)
    if elem == '/':
        if y == 0:
            print('divide by 0.')
            return
        else:
            return checkSat(x/y)
    if elem == '+':
        return checkSat(x+y)
    if elem == '-':
        return checkSat(x-y)
    if elem == '%':
        return checkSat(x%y)
    if elem == '^':
        return checkSat(x^y)

def acceptInput():
    while(1):
        isInfix = 0
        line = input('')
        for elem in line.split():
            if(elem.lstrip('-').isdigit()):
                addStack(checkSat(int(elem)))                
            else:   
                newelem = performOperation(elem)
                if newelem is not None:
                    addStack(newelem)
                else:
                    if not elem in validoperations: 
                        parseInfix(elem)
    return

validoperations = ['*','/','+','-','^','%','d','r','=']
stack = []
MAX = 2147483647
print('You can now begin using the SRPN calculator:')
acceptInput()