# Crie um sistema de login utilizando o tkinter e importando um banco de dados.
# A tarefa é criar 5 tipos diferentes de acesso (esses devem ser armazenados em banco), para cada acesso deve ser criada uma tela diferente de amostragem (uma imagem ou uma mensagem) quando o usuário colocar algum acesso que não existe no banco deve surgir uma mensagem avisando que este acesso não existe e perguntando se ele deseja criar um cadastro, se ele desejar deve ser feito o cadastro dele e enviado ao banco, caso o usuário digite a senha incorretamente deve surgir a mensagem de senha incorreta.
# O cadastro deve conter: usuário, senha e um texto que ele deseje armazenar em seu cadastro (se voce quiser um desafio maior pode armazenar uma imagem)
# Dica: https://acervolima.com/crie-uma-pagina-de-login-do-banco-de-dados-mysql-em-python-usando-tkinter/

import tkinter as tk
import mysql.connector
from tkinter import messagebox


# Conectar ao banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="Sim",
    password="",
    database="login_system"
)
cursor = db.cursor()

# Função para verificar login
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    
    if result:
        access_level = result[3]
        show_access_screen(access_level)
    else:
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        if cursor.fetchone():
            messagebox.showerror("Erro", "Senha incorreta!")
        else:
            if messagebox.askyesno("Cadastro", "Usuário não encontrado. Deseja criar um cadastro?"):
                create_user(username, password)

# Função para criar novo usuário
def create_user(username, password):
    extra_text = "Texto de exemplo"
    cursor.execute("INSERT INTO users (username, password, access_level, extra_text) VALUES (%s, %s, %s, %s)", 
                   (username, password, 1, extra_text))
    db.commit()
    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

# Função para mostrar a tela de acesso
def show_access_screen(access_level):
    if access_level == 1:
        messagebox.showinfo("Acesso", "Bem-vindo ao nível 1!")
    elif access_level == 2:
        messagebox.showinfo("Acesso", "Bem-vindo ao nível 2!")
    # Adicione mais níveis conforme necessário

# Interface Tkinter
root = tk.Tk()
root.title("Sistema de Login")

tk.Label(root, text="Usuário").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="Senha").grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2)

root.mainloop()


