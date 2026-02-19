import tkinter as tk

# main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("260x320")

# display
equation = ""
text = tk.StringVar()

entry = tk.Entry(root, textvariable=text, font=("Arial",18), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10)

# functions
def press(num):
    global equation
    equation = equation + str(num)
    text.set(equation)

def equal():
    global equation
    try:
        result = str(eval(equation))
        text.set(result)
        equation = result
    except:
        text.set("Error")
        equation = ""

def clear():
    global equation
    equation = ""
    text.set("")

# buttons
buttons = [
('7',1,0),('8',1,1),('9',1,2),('/',1,3),
('4',2,0),('5',2,1),('6',2,2),('*',2,3),
('1',3,0),('2',3,1),('3',3,2),('-',3,3),
('0',4,0),('C',4,1),('=',4,2),('+',4,3)
]

for (b,r,c) in buttons:
    if b == "=":
        tk.Button(root,text=b,width=5,height=2,command=equal).grid(row=r,column=c)
    elif b == "C":
        tk.Button(root,text=b,width=5,height=2,command=clear).grid(row=r,column=c)
    else:
        tk.Button(root,text=b,width=5,height=2,command=lambda x=b: press(x)).grid(row=r,column=c)

root.mainloop()
