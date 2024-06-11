''' A GUI displays objects that convey information, and represent actions that can be taken by user'''
from tkinter import *
from tkinter import ttk
root = Tk()
root.mainloop()

win = Tk() # win is a top or parent window
win.geometry('200x100')
b = Button(win, text = 'Submit')
b.pack() # using pack() geometry
win.mainloop()

root = Tk() # win is a top or parent window
label1 = Label(root, text = 'Hi welcome to GUI using Tkinter', fg = 'green')
label1.pack() # using pack() geometry
root.mainloop()

# To display several options in a form
root = Tk()
root.geometry('400x400')
c = Checkbutton(root, text = 'Python')
c.pack()
c1 = Checkbutton(root, text = 'C++')
c1.pack()
c2 = Checkbutton(root, text = 'C')
c2.pack()
root.mainloop()
