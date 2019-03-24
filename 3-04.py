'''
Created on Mar 7, 2019
Created for: ICS3U
@author: Francesca Berkoh
Daily Assignment - 3-04
This program determines a leap year
'''

from tkinter import *

root = Tk()

root.title("Leap Year")
root.geometry("200x400")

Welcome=Label(root, text= "Type a year")
Welcome.pack()

Yes = Label(root, text="It's a leap year!")
No = Label(root, text="It's not a leap year!")

TextBox = Entry(root)
TextBox.pack()


def Calculate():
    year_input = TextBox.get()
    year = int(year_input)
    if year % 100 == 0:
        if year % 400 == 0:
            Yes.pack()
        else:
            No.pack()
    else:
        if year % 4==0:
            Yes.pack()
        else:
            No.pack()

Check = Button(root, text="Leap Year?", command=Calculate)
Check.pack()        
        
root.mainloop()   

