import math as m

RAND = -1
commented = False

def rand(): #return a pseudorandom value
    global RAND
    #list of values output by c function rand(), up to 22nd value
    randNo = [1804289383,846930886,1681692777,1714636915,1957747793,424238335,719885386,1649760492,596516649,1189641421,1025202362,1350490027,783368690,1102520059,2044897763,1967513926,1365180540,1540383426,3040891721,303455736,35005211,521595368]
    if (RAND == 21): #loop round negative values
        RAND = 0
    else:
        RAND += 1
    return randNo[RAND]

def addStack(elem): #add element to stack
    if(len(stack) >= 23): #stack size is 23
        print('Stack Overflow')
    else:
        stack.append(elem)
    return

def checkSat(elem): #check if numbers are out of (int) value range, if they are then return max or min int value
    if elem > MAX:
        return MAX
    elif elem < -MAX:
        return -MAX
    else:
        return elem

def printStack(): #outputs the whole stack
    if len(stack) == 0: #if stack empty, print negative max
        print(-MAX)
        return
    for i in range(len(stack)):
        print(m.trunc(stack[i])) #print integer values of stack
    return

def parseInfix(input):
    infix = list(input)
    postfix,operators = ([] for i in range(2))
    for i in range(len(infix)): #iterate through infix string
        if infix[i].isdigit() and not commented: #if element is digit, add to postfix
            postfix.append(infix[i])
        elif infix[i] in validoperations:
            if infix[i] == '-' and (infix[i-1] in validoperations) and i != len(infix)-1: #if element is negative and previous element is an operator and not end of line, replace with unary negative placeholder 'n'
                infix[i] = 'n'
            while(not len(operators)==0) and (precedence.get(operators[-1],0) > precedence.get(infix[i],0)):
                postfix.append(operators.pop())
            operators.append(infix[i])
        else:
            print('Unrecognized operator or operand ',infix[i])
    while not(len(operators)==0):
        postfix.append(operators.pop())
    process(' '.join(postfix))
    return


def performOperation(elem): #perform postfix operations
    if not commented:
        #invalid operations
        if not elem in validoperations:
            return       
        #read-only operations
        if elem == 'd':
            printStack()
            return
        if elem == '=':
            print(m.trunc(stack[-1])) #print integer top of stack
            return
        if elem == 'r':
            return rand()
        #unary operation to return negative integer
        if elem == 'n':
            x = float(stack.pop())
            return -x
        #don't pop unless possible
        if(len(stack)>=2):
            y = float(stack.pop())
            x = float(stack.pop())
        else:
            print('Stack Underflow') #if not enough elements to pop, stack underflow
            return
        #write operations
        if elem == '*':
            return checkSat(x*y)
        if elem == '/':
            if y == 0: #avoid divide by 0 errors, return values to stack
                addStack(x)
                addStack(y)
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
            if y < 0: #avoid negative powers as output is integer
                addStack(x)
                addStack(y)
                print('Negative Power.')
                return
            return checkSat(x**y)

def process(line): #process input and add it to stack
    global commented
    #split space-separated input into array
    for elem in line.split():
        if(elem.replace('-','',1).isdigit() and not commented): #if element is negative/positive integer and not in a comment, add to stack
            addStack(checkSat(int(elem))) #add to stack and check saturation                
        else:
            #comment handling
            if commented and elem == '#':
                commented = 0
            elif not commented and elem == '#':
                commented = 1
            #attempt to execute operation
            elif not commented:   
                newelem = performOperation(elem)
                if newelem is not None:
                    addStack(newelem) #if operation executes, add to stack
                else:
                    if not elem in validoperations:  #if element is not valid postfix, try infix
                        parseInfix(elem)

def acceptInput(): #function that enables user input
    while(1):
        #accept input
        line = input('')
        process(line)
    return

validoperations = ['*','/','+','-','^','%','d','r','=','n'] #valid postfix operations

precedence = { #precedence of operations for infix
'^':5,
'd':5,
'n':5,
'%':4,
'/':3,
'*':2,
'+':1,
'-':1,
}

stack = [] #stack for evaluating postfix

MAX = 2147483647
print('You can now begin using the SRPN calculator:')
acceptInput() #begin accepting input