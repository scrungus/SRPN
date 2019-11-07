import math as m

def printStack():
    for i in range(len(stack)):
        print(stack[i])
    return

def performOperation(elem):
    validoperations = ['*','/','+','-','^','%','d','r','=']
    if not elem in validoperations:
        print('unrecognised operator ',elem)
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
    y = float(stack.pop())
    x = float(stack.pop())
    if elem == '*':
        return x*y
    if elem == '/':
        return x/y
    if elem == '+':
        return x+y
    if elem == '-':
        return x-y
    if elem == '%':
        return x%y
    if elem == '^':
        return x^y

def acceptInput():
    while(1):
        line = input('')
        for elem in line.split():
            if elem.isdigit() :
                stack.append(elem)
            else:
                newelem = performOperation(elem)
                if newelem is not None:
                    stack.append(newelem)
    return

stack = []
print('You can now begin using the SRPN calculator:')
acceptInput()