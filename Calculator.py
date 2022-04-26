"""
    Author: Aritra Bhattacharjee
    Date of Working: 25.04.2022 to 26.04.2022
    Tech Stack: Python, Tkinter.
    About: A python based calculator.
"""
from tkinter import *

class Calculator(Tk):    
    
    def __init__(self) :
        super().__init__()
        self.geometry("320x350")
        self.title("Calculator")

        self.wm_iconbitmap("Calc.ico")
        self.expression=""
        self.input_text = StringVar()

        # frame for the input fields
        self.input_frame = Frame(self,width=312,height=50)
        self.input_frame.pack(side=TOP)

        self.input_field = Entry(self.input_frame,textvariable=self.input_text,font="lucida 20 bold",justify=RIGHT)
        self.input_field.grid(row=0,column=0)
        self.input_field.pack(ipady=10)

        # frame for the buttons
        btns_frame = Frame(self,width=310, height=270,bg="grey")
        btns_frame.pack()
        # row 1
        clear = Button(btns_frame,text="C",fg="black",width=32,height=3,cursor="hand2",command=lambda:self.clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

        divide = Button(btns_frame,text="/",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click('/')).grid(row = 0, column = 3, padx = 1, pady = 1)

        # row 2
        seven =Button(btns_frame,text="7",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)

        eight =Button(btns_frame,text="8",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)

        nine =Button(btns_frame,text="9",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

        multiply=Button(btns_frame,text="*",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
        # row 3
        four =Button(btns_frame,text="4",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)

        five =Button(btns_frame,text="5",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)

        six=Button(btns_frame,text="6",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

        minus = Button(btns_frame,text="-",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
        # row 4
        one =Button(btns_frame,text="1",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)

        two  =Button(btns_frame,text="2",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)

        three =Button(btns_frame,text="3",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

        plus = Button(btns_frame,text="+",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

        # fourth row
        zero= Button(btns_frame,text="0",fg="black",width=21,height=3,cursor="hand2",command=lambda:self.click("0")).grid(row = 4, column = 0,columnspan=2, padx = 1, pady = 1)

        point=Button(btns_frame,text="+",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.click("+")).grid(row = 4, column = 2, padx = 1, pady = 1)

        equals=Button(btns_frame,text="=",fg="black",width=10,height=3,cursor="hand2",command=lambda:self.equals()).grid(row = 4, column = 3, padx = 1, pady = 1)

    def click(self,event):
        self.expression = self.expression+str(event)
        self.input_text.set(self.expression)
        
    def equals(self):
        result = str(eval(self.expression))
        self.input_text.set(result)
        self.expression=f"{result}"

    def clear(self):
        self.expression=""
        self.input_text.set("")
        

    

if __name__=='__main__':
    
    obj = Calculator()
    obj.mainloop()
