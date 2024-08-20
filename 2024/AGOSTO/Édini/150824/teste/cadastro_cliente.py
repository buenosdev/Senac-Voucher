from tkinter import *

def on_focus_in(event):
    """Função para ocultar o label associado ao campo de entrada quando o campo recebe foco."""
    widget = event.widget
    if widget == user:
        label_user.grid_forget()
    elif widget == senha1:
        label_senha1.grid_forget()
    elif widget == senha2:
        label_senha2.grid_forget()

def on_focus_out(event):
    """Função para restaurar o label associado ao campo de entrada quando o campo perde o foco, se estiver vazio."""
    widget = event.widget
    if widget == user:
        if not user.get():
            label_user.grid(row=1, column=1, padx=10, pady=10)
    elif widget == senha1:
        if not senha1.get():
            label_senha1.grid(row=2, column=1, padx=10, pady=10)
    elif widget == senha2:
        if not senha2.get():
            label_senha2.grid(row=3, column=1, padx=10, pady=10)

#Função para validar a senha           
def validate():
    """Função para validar os campos de entrada."""
    user_input = user.get()
    senha_input = senha1.get()
    senha_confirm = senha2.get()

    # Verifica se todos os campos estão preenchidos
    if not user_input:
        print("O campo Usuário está vazio.")
        return
    if not senha_input:
        print("O campo Senha está vazio.")
        return
    if not senha_confirm:
        print("O campo Confirmação de Senha está vazio.")
        return
    
    # Verifica se a senha e a confirmação de senha coincidem
    if senha_input != senha_confirm:
        print("A confirmação da senha não coincide com a senha.")
        return
    
    # Se todas as validações passaram
    print("Todos os campos estão preenchidos e as senhas coincidem!")


root = Tk()

frm = Frame(root, bg='lightblue', padx=200, pady=200)
frm.grid()

Label(frm, text="Cadastre-se no meu sistema :D", font=("Arial", 50), fg='purple', bg='lightblue').grid(column=1, row=0, padx=10, pady=10)

# Usuário
user = Entry(frm, font=('Arial', 20))
user.grid(column=1, row=1, padx=10, pady=10)

label_user = Label(frm, text="Usuário", font=("Arial", 18), fg='black', bg='white')
label_user.grid(column=1, row=1, padx=10, pady=10)

# Senha
senha1 = Entry(frm, font=('Arial', 20), show='*')  
senha1.grid(column=1, row=2, padx=10, pady=10)

label_senha1 = Label(frm, text="Senha", font=("Arial", 18), fg='black', bg='white')
label_senha1.grid(column=1, row=2, padx=10, pady=10)

# Confirmação de Senha
senha2 = Entry(frm, font=('Arial', 20), show='*')  
senha2.grid(column=1, row=3, padx=10, pady=10)

label_senha2 = Label(frm, text="Confirme a Senha", font=("Arial", 18), fg='black', bg='white')
label_senha2.grid(column=1, row=3, padx=10, pady=10)

# Associar eventos de foco aos campos de entrada
user.bind('<FocusIn>', on_focus_in)
user.bind('<FocusOut>', on_focus_out)

senha1.bind('<FocusIn>', on_focus_in)
senha1.bind('<FocusOut>', on_focus_out)

senha2.bind('<FocusIn>', on_focus_in)
senha2.bind('<FocusOut>', on_focus_out)





Button(frm, text="Cadastrar", font=('Arial', 20), bg='purple', fg='white').grid(column=1, row=4, padx=10, pady=10)

root.mainloop()
