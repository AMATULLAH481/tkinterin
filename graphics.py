from tkinter import *
# import tkinter as tk
root = Tk()
root.title("My Tkinter App")
label = Label(root, text="Hello, Amatullah", bg="yellow").pack()
label2 = Label(root, text = "Your first GUI code !!").pack()
# label.grid(row=0, column=1)
# label2.grid(row= 1, column= 2)
mybutton = Button(root, text= "Click me!", padx=50,pady=20,bg="pink")
mybutton.pack()

root.mainloop()