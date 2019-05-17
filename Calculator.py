import tkinter
from math import *
expression = ""
ans = ""
def buttonPressed(event, numStr):
    global expression
    expression += numStr
    equation.set(expression)

def clearPressed(event):
    global expression
    expression = ""
    equation.set(expression)


def equalPressed(event):
    global expression
    global ans
    try:
        user_total = eval(expression)
        equation.set(user_total)
        ans = user_total
        expression = ""
    except:
        equation.set("Error")
        expression = ""


def ansPressed():
    global expression
    global ans
    buttonPressed(None,str(ans))



calculatorWindow = tkinter.Tk()


calculatorWindow.title("CALCULATOR")


calculatorWindow.geometry("375x200")

equation = tkinter.StringVar()

user_expression = tkinter.Entry(calculatorWindow, text = equation)

user_expression.grid(columnspan=4, ipadx=70)
expression = str(user_expression.get())

button1 = tkinter.Button(calculatorWindow, text = "1",  command = lambda:  buttonPressed(None,"1"))
button1.grid(row=2, column=0)

button2 = tkinter.Button(calculatorWindow, text = "2",  command = lambda:  buttonPressed(None,"2"))
button2.grid(row=2, column=1)

button3 = tkinter.Button(calculatorWindow, text = "3",  command = lambda: buttonPressed(None,"3"))
button3.grid(row=2, column=2)

button4 = tkinter.Button(calculatorWindow, text = "4",  command = lambda: buttonPressed(None,"4"))
button4.grid(row=3, column=0)

button5 = tkinter.Button(calculatorWindow, text = "5",  command = lambda: buttonPressed(None,"5"))
button5.grid(row=3, column=1)

button6 = tkinter.Button(calculatorWindow, text = "6",  command = lambda: buttonPressed(None,"6"))
button6.grid(row=3, column=2)

button7 = tkinter.Button(calculatorWindow, text = "7",  command = lambda: buttonPressed(None,"7"))
button7.grid(row=4, column=0)

button8 = tkinter.Button(calculatorWindow, text = "8",  command = lambda: buttonPressed(None,"8"))
button8.grid(row=4, column=1)

button9 = tkinter.Button(calculatorWindow, text = "9",  command = lambda: buttonPressed(None,"9"))
button9.grid(row=4, column=2)

button0 = tkinter.Button(calculatorWindow, text = "0",  command = lambda: buttonPressed(None,"0"))
button0.grid(row=5, column=0)

buttonPlus = tkinter.Button(calculatorWindow, text = "+",  command = lambda: buttonPressed(None,"+"))
buttonPlus.grid(row=2, column=3)

buttonSubtract = tkinter.Button(calculatorWindow, text = "-",  command = lambda: buttonPressed(None,"-"))
buttonSubtract.grid(row=3, column=3)

buttonMultiply = tkinter.Button(calculatorWindow, text = "*",  command = lambda: buttonPressed(None,"*"))
buttonMultiply.grid(row=4, column=3)

buttonDivide = tkinter.Button(calculatorWindow, text = "/",  command = lambda: buttonPressed(None,"/"))
buttonDivide.grid(row=5, column=3)

buttonClear = tkinter.Button(calculatorWindow, text = "CLEAR",  command = lambda: clearPressed(None))
buttonClear.grid(row=5, column=1)

buttonEqual = tkinter.Button(calculatorWindow, text = "=",  command = lambda: equalPressed(None))
buttonEqual.grid(row=5, column=2)




buttonAns = tkinter.Button(calculatorWindow, text = "ANS",  command = lambda: ansPressed())
buttonAns.grid(row=6, column=0)

buttonOpenParenthese = tkinter.Button(calculatorWindow, text = "(",  command = lambda: buttonPressed(None,"("))
buttonOpenParenthese.grid(row=6, column=1)

buttonCloseParenthese = tkinter.Button(calculatorWindow, text = ")",  command = lambda: buttonPressed(None,")"))
buttonCloseParenthese.grid(row=6, column=2)

safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
             'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
             'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
             'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
             'tan', 'tanh']


safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])

calculatorWindow.bind('<Return>', equalPressed)
calculatorWindow.bind('<BackSpace>', clearPressed)
calculatorWindow.bind('1', lambda event, arg='1': buttonPressed(event, arg))
calculatorWindow.bind('2', lambda event, arg='2': buttonPressed(event, arg))
calculatorWindow.bind('3', lambda event, arg='3': buttonPressed(event, arg))
calculatorWindow.bind('4', lambda event, arg='4': buttonPressed(event, arg))
calculatorWindow.bind('5', lambda event, arg='5': buttonPressed(event, arg))
calculatorWindow.bind('6', lambda event, arg='6': buttonPressed(event, arg))
calculatorWindow.bind('7', lambda event, arg='7': buttonPressed(event, arg))
calculatorWindow.bind('8', lambda event, arg='8': buttonPressed(event, arg))
calculatorWindow.bind('9', lambda event, arg='9': buttonPressed(event, arg))
calculatorWindow.bind('0', lambda event, arg='0': buttonPressed(event, arg))
calculatorWindow.bind('+', lambda event, arg='+': buttonPressed(event, arg))
calculatorWindow.bind('-', lambda event, arg='-': buttonPressed(event, arg))
calculatorWindow.bind('/', lambda event, arg='/': buttonPressed(event, arg))
calculatorWindow.bind('*', lambda event, arg='*': buttonPressed(event, arg))
calculatorWindow.bind('(', lambda event, arg='(': buttonPressed(event, arg))
calculatorWindow.bind(')', lambda event, arg=')': buttonPressed(event, arg))

calculatorWindow.mainloop()