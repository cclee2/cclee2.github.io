#-------------------------------------------
#Bradley Missakian
#Christopher Lee
#Period 2
#------------------------------------------
#disclaimer the answers will be rounded to the nearest whole number
from Tkinter import*
#imported Tkinter which is able to make a GUI

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
#Function lets you click the buttons to be able to put the numbers in the display    

def btnClearDisplay():
    global operator 
    operator=""
    text_Input.set("")
#This function lets you clear the display when numbers are present

def btnEpualsInput():
    global operator 
    addup=str(eval(operator))
    text_Input.set(addup)
    operator=""
#Function allows the user to have the sum of an equation
    
cal = Tk()
cal.title("Calculator")
operator=""
text_Input =StringVar()
#This allows the user to see and input numbers in the display

txtDisplay = Entry(cal,font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="lightgrey", justify='right') .grid(columnspan=4)
#This is the GUI display for the calculator


btn7=Button(cal,padx=16,bd=8, fg="white",font=('arial', 20, 'bold'),text="7",bg="black",command=lambda:btnClick(7)) .grid(row=1,column=0)

btn8=Button(cal,padx=16,bd=8, fg="white",font=('arial', 20, 'bold'),text="8",bg="black",command=lambda:btnClick(8)) .grid(row=1,column=1)

btn9=Button(cal,padx=16,bd=8, fg="white",font=('arial', 20, 'bold'),text="9",bg="black",command=lambda:btnClick(9)) .grid(row=1,column=2)

Addition=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),text="+",bg="grey",command=lambda:btnClick("+")) .grid(row=1,column=3)

#=======================================================================================================

btn4=Button(cal,padx=16,bd=8, fg="white",font=('arial', 20, 'bold'),text="4",bg="black",command=lambda:btnClick(4)) .grid(row=2,column=0)

btn5=Button(cal,padx=16,bd=8, fg="white",font=('arial', 20, 'bold'),text="5",bg="black",command=lambda:btnClick(5)) .grid(row=2,column=1)

btn6=Button(cal,padx=16,bd=8, fg="white",font=('arial', 20, 'bold'),text="6",bg="black",command=lambda:btnClick(6)) .grid(row=2,column=2)

Subtraction=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),text="-",bg="grey",command=lambda:btnClick("-")) .grid(row=2,column=3)

#=======================================================================================================

btn1=Button(cal,padx=16,bd=8, fg="white",font=('arial', 20, 'bold'),text="1",bg="black",command=lambda:btnClick(1)) .grid(row=3,column=0)

btn2=Button(cal,padx=16,bd=8, fg="white",font=('arial', 20, 'bold'),text="2",bg="black",command=lambda:btnClick(2)) .grid(row=3,column=1)

btn3=Button(cal,padx=16,bd=8, fg="white",font=('arial', 20, 'bold'),text="3",bg="black",command=lambda:btnClick(3)) .grid(row=3,column=2)

Multiplication=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),text="*",bg="grey",command=lambda:btnClick("*")) .grid(row=3,column=3)

#=======================================================================================================

btn0=Button(cal,padx=16,bd=8, fg="white",font=('arial', 20, 'bold'),text="0",bg="black",command=lambda:btnClick(0)) .grid(row=4,column=0)

btnCE=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),text="C",bg="darkorange", command= btnClearDisplay) .grid(row=4,column=1)

btnEquals=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20, 'bold',),text="=", bg="darkorange",command=btnEpualsInput) .grid(row=4,column=2)

Division=Button(cal,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),text="/",bg="grey",command=lambda:btnClick("/")) .grid(row=4,column=3)
#All of these codes are for the calculator which shows each digit and each mathmatical symbol



cal.mainloop()
#main