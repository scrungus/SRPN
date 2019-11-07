import math as m

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

def findOffender(elem):
    for i in range(len(elem)):
        if not elem[i].isdigit():
            return elem[i]

def performOperation(elem):
    #invalid operations
    if not elem in validoperations:
        print('unrecognised operator',findOffender(elem))

        try:
            return float(elem)
        except:
            return
    #read-only operations
    if elem == 'd':
        printStack()
        return
    if elem == '=':
        print(m.trunc(stack[-1]))
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
        line = input('')
        for elem in line.split():
            if(elem.lstrip('-').isdigit()):
                stack.append(checkSat(int(elem)))
                
            else:
                newelem = performOperation(elem)
                if newelem is not None:
                    stack.append(newelem)
    return

validoperations = ['*','/','+','-','^','%','d','r','=']
stack = []
MAX = 2147483647
print('You can now begin using the SRPN calculator:')
acceptInput()