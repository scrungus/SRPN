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

def performOperation(elem):
    validoperations = ['*','/','+','-','^','%','d','r','=']
    if not elem in validoperations:
        print('unrecognised operator ',)
        try:
            return float(elem)
        except:
            return

    if elem == 'd':
        printStack()
        return
    if elem == '=':
        print(m.trunc(stack[-1]))
        return
    try:
        y = float(stack.pop())
        x = float(stack.pop())
    except:
        print('Stack Underflow')
        stack.append(y)
        return

    if elem == '*':
        return checkSat(x*y)
    if elem == '/':
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
            try:
                stack.append(checkSat(float(elem)))
            except:
                newelem = performOperation(elem)
                if newelem is not None:
                    stack.append(newelem)
    return

stack = []
MAX = 2147483647
print('You can now begin using the SRPN calculator:')
acceptInput()