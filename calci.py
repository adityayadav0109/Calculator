from tkinter import *

root = Tk()

root.geometry("1050x720")
root.maxsize(1050,720)
root.minsize(1050,720)
root.title('Calculator by Aditya')
root.wm_iconbitmap("logo.ico")

def click(event):
    global blank_space_var
    inpt = event.widget.cget('text')
    if inpt == "=":
        if blank_space_var.get().isdigit():
            value = int(blank_space_var.get())
        else:
            value = eval(blank_space.get())
        blank_space_var.set(value)
        
    elif inpt == "C":
        blank_space_var.set("")
    
    else:
        blank_space_var.set(blank_space_var.get() + inpt)


blank_space_var = StringVar()
blank_space_var.set('')

blank_space = Entry(root, textvariable = blank_space_var, font = 'ubantu 50 bold', fg = 'red')

blank_space.pack(fill = X, padx = 20, pady = 10)


f1 = Frame(root, bg = 'cyan', pady = 10)
f1.pack(fill = X)

buttu = Button(f1, text = '1', fg = "white", bg = 'red', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f1, text = '2', fg = "white", bg = 'red', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20,ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f1, text = '3', fg = "white", bg = 'red', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f1, text = '*', fg = "white", bg = 'orange', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f1, text = '+', fg = "white", bg = 'orange', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f1, text = '-', fg = "white", bg = 'orange', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 30)
buttu.bind("<Button-1>",click)


f2 = Frame(root, bg = 'cyan', pady = 10)
f2.pack(fill = X)

buttu = Button(f2, text = '4', fg = "white", bg = 'red', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f2, text = '5', fg = "white", bg = 'red', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f2, text = '6', fg = "white", bg = 'red', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)



f3 = Frame(root, bg = 'cyan', pady = 10)
f3.pack(fill = X)

buttu = Button(f3, text = '7', fg = "white", bg = 'red', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f3, text = '8', fg = "white", bg = 'red', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20,ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f3, text = '9', fg = "white", bg = 'red', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f3, text = '/', fg = "white", bg = 'orange', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f3, text = '=', fg = "white", bg = 'orange', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20,ipadx = 20)
buttu.bind("<Button-1>",click)

buttu = Button(f3, text = 'C', fg = "white", bg = 'orange', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 20, ipadx = 20)
buttu.bind("<Button-1>",click)



f4 = Frame(root, bg = 'cyan', pady = 10)
f4.pack(fill = X)

buttu = Button(f4, text = '0', fg = "white", bg = 'red', font = 'ubantu 50 bold')
buttu.pack(side = LEFT, padx = 200, ipadx = 20)
buttu.bind("<Button-1>",click)
root.config(bg = 'cyan')




root.mainloop()