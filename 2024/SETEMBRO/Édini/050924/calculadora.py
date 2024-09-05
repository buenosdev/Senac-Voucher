import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')

root = tk.Tk()
root.title("Calculadora")

# Define o fundo da janela como preto
root.configure(bg='black')

entry = tk.Entry(root, width=22, font=('Arial', 24), borderwidth=3, relief="solid", bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Define o estilo dos botões
button_style = {
    'font': ('Arial', 16, 'bold'),
    'bg': '#333333',
    'fg': '#ffffff', 
    'relief': 'raised',
    'bd': 1
}

row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        b = tk.Button(root, text=button, width=7, height=3, command=calculate, **button_style)
    else:
        b = tk.Button(root, text=button, width=7, height=3, command=lambda b=button: click_button(b), **button_style)
    b.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_button = tk.Button(root, text='C', width=7, height=3, command=clear, **button_style)
clear_button.grid(row=row_val, column=col_val)

root.mainloop()
