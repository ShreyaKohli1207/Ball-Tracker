from tkinter import *
from tkinter.ttk import *

#File title
window = Tk() 
window.title("Ball Tracker")

#Geometry
window.geometry('600x300')


#Label For file path
lbl = Label(window, text="Enter file path(Optional)")
lbl.grid(column=0, row=2)

#Text Field
vidpath = Entry(window, width=30)
vidpath.grid(column=1, row=2)

#Label for ball color
lbl = Label(window, text="Select Ball Color")
lbl.grid(column=0, row=4)


#radiobutton
selected = IntVar()
rad1 = Radiobutton(window,text='Black', value=1, variable=selected)
rad2 = Radiobutton(window,text='Green', value=2, variable=selected)
rad3 = Radiobutton(window,text='White', value=3, variable=selected)

rad1.grid(column=0, row=6)
rad2.grid(column=0, row=7)
rad3.grid(column=0, row=8)

#Define run button
def clicked():
    print(selected.get())
    print("File path is :"+vidpath.get() )

#Button
strt = Button(window, text="Run Program", command=clicked)
strt.grid(column=1, row=0)

ext = Button(window, text="Exit")
ext.grid(column=2, row=0)

window.mainloop() 
