
# Simple example multiply function name

def multiply():

    result = 10 * 4
    return result  # return the value

def multiply_para(x, y):
    result = x * y
    return result  # return the value

answer = multiply()
print(answer)
print()
print(" value without parameter fn:  answer is {}".format(answer))
print("*" *40)
answer_para = multiply_para(10,4)
print(" same value by parameter fn: answer_para is: {}".format(answer_para))
print("*" *40)
for val in range (1,11):
    twice = multiply_para(2,val)
    print("twice times of {} is {}".format(val, twice))

# Doc string
# To specify the parameter types, follow these general steps﻿
# Press CtrlAlt S
#  and go to Editor | General |Smart Keys.
#
# Select the Insert type placeholders checkbox in the Smart Keys page of the editor settings.
#
# Place the caret at the function name, and press AltEnter.
#
# In the list of intention actions that opens, choose Insert documentation string stub. PyCharm creates a documentation stub, according to the selected docstring format, with the type specification, collected during the debugger session.