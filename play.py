from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()

notebook = ttk.Notebook(root)
notebook.grid(column=0, row=0)

frame1 = Frame(notebook, width=200, height=200)
frame2 = Frame(notebook, width= 200, height=200)

notebook.add(frame1, text='#1')
notebook.add(frame2, text='#2')


img = ImageTk.PhotoImage(Image.open('1.ico'))

lab1 = Label(frame1, image=img)
lab2 = Label(frame2, text='frame 2')


lab1.grid(column=0, row=0)
lab2.grid(column=0, row=0)    


# piclabel = Label(root, image=img)
# piclabel.grid(row=0, column=0)



root.mainloop()

