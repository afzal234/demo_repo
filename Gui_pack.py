from tkinter import *
# creating TK window
pane =Tk()

b1 = Button(pane,text="Click me!")
b1.pack(fill=Y,expand = True)

# Button 2
b2 = Button(pane,text="Click me too")
b2.pack(fill=X,expand = True)

# Execute Tkinter
pane.mainloop()