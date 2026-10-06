import tkinter

# window = tkinter.Tk()
# window.title('MY-GUI')

# lab = tkinter.Label(window, text = "WELCOME TO PYTHON ADVANCED", bg = 'Purple', fg = 'Green').pack()

# lab1 = tkinter.Label(text = "THIS IS MY FIRST CLASS ON GUI", fg = 'Red').pack()

# txt = tkinter.Entry(width = 20).pack()

# txt1 = tkinter.Text().pack()

# btn = tkinter.Button(text = 'Click Here!', bg = 'Pink').pack()


# window.mainloop()

screen = tkinter.Tk()
screen.title('PYTHON')
screen.geometry('500x300')
screen.configure(bg = 'Pink')

lab = tkinter.Label(screen, text = 'WELCOME TO CLASS!!!').pack()

name = tkinter.Label(text = 'Name').place(x = 30, y = 50)
email = tkinter.Label(text = 'Email').place(x = 30, y = 90)

n_ent = tkinter.Entry().place(x = 80, y = 50)
e_ent = tkinter.Entry().place(x = 80, y = 90)










screen.mainloop()