from ArrayStack import *

def postfix_calculator():
    operators = "+-*/%"
    mydict = {}

    while True:
        inputs = input('--> ')
        if inputs == 'done()':
            break
    
        if "=" in inputs:
            seperate = inputs.split(" = ")
            val = seperate[0]
            lst = seperate[1].split(" ")
            stack = ArrayStack()

            for elem in lst:
                if elem not in operators:
                    if elem.isalpha():
                        if elem in mydict:
                            stack.push(mydict[elem])
                    else:
                        stack.push(float(elem))
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    if elem == '+':
                        put = val2 + val1
                        stack.push(put)
                    elif elem == '-':
                        put = val2 - val1
                        stack.push(put)
                    elif elem == '*':
                        put = val2 * val1
                        stack.push(put)
                    elif elem == '/':
                        if val1 == 0:
                            raise ZeroDivisionError
                        stack.push(val2 / val1)

            mydict[val] = stack.top()
            print(val)

        else:
            lst = inputs.split()
            stack = ArrayStack()

            for elem in lst:
                if elem not in operators:
                    if elem.isalpha():
                        if elem in mydict:
                            stack.push(mydict[elem])
                    else:
                        stack.push(float(elem))
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    if elem == '+':
                        put = val2 + val1
                        stack.push(put)
                    elif elem == '-':
                        put = val2 - val1
                        stack.push(put)
                    elif elem == '*':
                        put = val2 * val1
                        stack.push(put)
                    elif elem == '/':
                        if val1 == 0:
                            raise ZeroDivisionError
                        stack.push(val2 / val1)

            print(stack.top())



postfix_calculator()