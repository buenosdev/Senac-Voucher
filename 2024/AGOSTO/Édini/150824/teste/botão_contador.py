from tkinter import *
from tkinter import ttk

contador = 0

def cont():
    global contador
    contador= contador + 1 
    if (contador==1):
        print("O botão foi clicado ", contador, " vez")
    else:
        print("O botão foi clicado ", contador, " vezes")

root = Tk()

frm = Frame(root, bg='lightblue', padx=200, pady=200)
frm.grid()


Label(frm, text="Clique no botão" ,font=("Arial",60), fg='purple', bg= 'lightblue').grid(column=1, row=0)
Button(frm, text="Botão", command=cont, font=('Arial', 30), bg='purple', fg='white').grid(column=1, row=1)


root.mainloop()
