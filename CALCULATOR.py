from tkinter import *

window=Tk()
expression = ""
equation = StringVar()
topEq = StringVar()




window.geometry("500x1000")
window.title("CALCULATOR")
window.config(bg="blue")
w=Label(window,text="welcome",width="45",height="45")
entry=Entry(window,width="35",bd="5",textvariable=topEq)



def add_chr(num):
    global expression
    expression +=str(num)
    topEq.set(expression)

def pressEquate(equate):
    global expression
    if (expression == ""):
        expression = ""
    else:
        expression += str(equate)
    topEq.set(expression)

def press_clear():
    global expression
    expression=""
    topEq.set(expression)
    equation.set(expression)

def pressEqual():
    global expression
    total = str(eval(expression))
    equation.set(total)










button7=Button(window,text="7",width="10",height="5",command=lambda:add_chr(7))
button8=Button(window,text="8",width="10",height="5",command=lambda:add_chr(8))
button9=Button(window,text="9",width="10",height="5",command=lambda:add_chr(9))

button4=Button(window,text="4",width="10",height="5",command=lambda:add_chr(4))
button5=Button(window,text="5",width="10",height="5",command=lambda:add_chr(5))
button6=Button(window,text="6",width="10",height="5",command=lambda:add_chr(6))

button1=Button(window,text="1",width="10",height="5",command=lambda:add_chr(1))
button2=Button(window,text="2",width="10",height="5",command=lambda:add_chr(2))
button3=Button(window,text="3",width="10",height="5",command=lambda:add_chr(3))

button_CLEAR=Button(window,text="CLEAR",width="10",height="5",bg="red",command=lambda:press_clear())
button_Add=Button(window,text="+",width="10",height="5", command=lambda: pressEquate("+"))
button_mul=Button(window,text="*",width="10",height="5", command=lambda: pressEquate("*"))

button_sub=Button(window,text="-",width="10",height="5",command=lambda: pressEquate("-"))
button_Equal=Button(window,text="=",width="10",height="5",command=pressEqual)
button_div=Button(window,text="/",width="10",height="5",command=lambda: pressEquate("/"))





entry.grid(row=0,padx=150, pady=20,columnspan="3")

button7.grid(row=1,column=0,padx=20, pady=20)
button8.grid(row=1,column=1,padx=20, pady=20)
button9.grid(row=1,column=2,padx=20, pady=20)

button4.grid(row=2,column=0,padx=20, pady=20)
button5.grid(row=2,column=1,padx=20, pady=20)
button6.grid(row=2,column=2,padx=20, pady=20)

button1.grid(row=3,column=0,padx=20, pady=20)
button2.grid(row=3,column=1,padx=20, pady=20)
button3.grid(row=3,column=2,padx=20, pady=20)

button_mul.grid(row=4,column=0,padx=20, pady=20)
button_Add.grid(row=4,column=1,padx=20, pady=20)
button_div.grid(row=4,column=2,padx=20, pady=20)

button_sub.grid(row=5,column=0,padx=20, pady=20)
button_Equal.grid(row=5,column=1,padx=20, pady=20)
button_CLEAR.grid(row=5,column=2,padx=20, pady=20)









window.mainloop()