import math as m

RAND = -1

def rand():
    global RAND
    randNo = [1804289383,846930886,1681692777,1714636915,1957747793,424238335,719885386,1649760492,596516649,1189641421,1025202362,1350490027,783368690,1102520059,2044897763,1967513926,1365180540,1540383426,3040891721,303455736,35005211,521595368]
    if (RAND == 21):
        RAND = 0
    RAND += 1
    return randNo[RAND]

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
        return rand()
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