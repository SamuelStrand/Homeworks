from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=200)
root.title("Заголовок окна программы")
root.geometry("640x480")
frm.grid()

def write():
    print("Все работает хорошо")

# Это пустая кнопка, чтобы сделать отступ
Button(
       padx = 100,
       pady = 40,
       border=0,
       ).grid(column=1, row =1 )


Button(text = "Это кнопка",
       foreground="blue",
       padx = 100,
       pady = 40,
       command=write,
       ).grid(column=2, row =1 )


root.mainloop()