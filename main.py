import math as m

RAND = -1 #random number index
commented = False #for persistent multi-line comments

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

def parseInfix(input): #attempts to parse infix notation
    infix = list(input)
    postfix,operators = ([] for i in range(2))
    i = 0 
    while i < len(infix): #iterate through infix string
        if (infix[i].isdigit() or infix[i]=='r') and not commented: #if element is digit, add to postfix
            number = ''
            while(i<len(infix)): #add digits until coming to end or an operator - for multi-digit numbers
                number += infix[i]
                i+=1
                if i==len(infix) or not infix[i].isdigit() :
                    i -=1
                    postfix.append(number)
                    break
        elif infix[i] in validoperations: #if operator is valid
            if (infix[i] == '-' and ((infix[i-1] in validoperations) and i != len(infix)-1)) or(infix[i] == '-' and i==0)  : #if element is negative and previous element is an operator and not end of line, or if '-' is first element on line, replace with unary negative placeholder 'n'
                infix[i] = 'n'
            while(not len(operators)==0) and (precedence.get(operators[-1],0) > precedence.get(infix[i],0)): #while operators on stack are higher precedence than current operator, pop these off and add them to the postfix string so they execute first
                postfix.append(operators.pop())
            operators.append(infix[i]) #add new operator to stack
        else: #invalid operator
            print('Unrecognized operator or operand ',infix[i])
        i+=1
    while not(len(operators)==0): #append remaining operators
        postfix.append(operators.pop())
    process(' '.join(postfix)) #process postfix - join converts list back to string which process() can use
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
        if elem == '*': #catching OverflowError, which can be thrown if x*y is too big
            try:
                return checkSat(x*y)
            except:
                if (x>0 and y>0) or (y<0 and x<0):
                    return MAX
                return -MAX
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
            try: #catching OverflowError, which can be thrown if x^y is too big
                return checkSat(x**y)
            except:
                if x<0:
                    if y%2==0:
                        return MAX
                    else:
                        return -MAX
                return MAX

def process(line): #process input and add it to stack
    global commented
    #split space-separated input into array
    for elem in line.split():
        if(elem.isdigit() and not commented): #if element is negative/positive integer and not in a comment, add to stack
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
        if('n' in line):
            print('Unrecognized operator or operand n' )
        process(line.replace('n','')) #don't allow user input of special negation character
    return

validoperations = ['*','/','+','-','^','%','d','r','=','n'] #valid postfix operations

precedence = { #precedence of operations for infix
'=':6,
'^':5,
'n':5,
'%':4,
'/':3,
'*':2,
'+':1,
'-':1,
}

stack = [] #stack for evaluating postfix

MAX = 2147483647 #max int size
print('You can now begin using the SRPN calculator:')
acceptInput() #begin accepting input