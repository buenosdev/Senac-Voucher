import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Importando Pillow para manipulação de imagens

# Tamanho padrão das imagens
IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100

# Função para validar a senha
def validar_senha(senha, confirmar_senha):
    if senha != confirmar_senha:
        return False, "As senhas não coincidem."
    if len(senha) < 1:
        return False, "A senha deve ter pelo menos 8 caracteres."
    if not any(char.isdigit() for char in senha):
        return False, "A senha deve conter pelo menos um número."
    if not any(char.isupper() for char in senha):
        return True, "A senha deve conter pelo menos uma letra maiúscula."
    return True, ""

# Função para redimensionar imagens
def carregar_imagem(caminho):
    try:
        imagem = Image.open(caminho)
        imagem = imagem.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
        return ImageTk.PhotoImage(imagem)
    except Exception as e:
        print(f"Erro ao carregar a imagem {caminho}: {e}")
        return None

# Função para logar
def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    confirmar_senha = entry_confirmar_senha.get()

    valido, mensagem = validar_senha(senha, confirmar_senha)
    if not valido:
        messagebox.showerror("Erro", mensagem)
    else:
        messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
        janela_login.destroy()
        tela_inicial(usuario)

# Função para criar a tela inicial
def tela_inicial(usuario):
    janela_inicial = tk.Tk()
    janela_inicial.title("Tela Inicial")
    janela_inicial.geometry("800x600")

    # Saudação
    lbl_ola = tk.Label(janela_inicial, text=f"Olá, {usuario}", font=("Helvetica", 20, "bold"), fg="#000000")
    lbl_ola.pack(pady=20)

    categorias = ["Entradas", "Pratos Principais", "Bebidas", "Bebidas Alcoólicas", "Sobremesas", "Menu do Chef"]

    # Card de menu
    card_frame = tk.Frame(janela_inicial)
    card_frame.pack(pady=20)

    estilo_botao = ttk.Style()
    estilo_botao.configure("TButton", font=("Helvetica", 14), padding=10, background="#C0C0C0", foreground="#000000")

    # Hover nos botões
    estilo_botao.map("TButton",
                     foreground=[("active", "#000000")],
                     background=[("active", "#A0A0A0")])

    for categoria in categorias:
        btn_categoria = ttk.Button(card_frame, text=categoria, style="TButton",
                                   command=lambda c=categoria: tela_categoria(c))
        btn_categoria.pack(pady=10, padx=20, fill=tk.X)

    janela_inicial.mainloop()

# Função para criar a tela de categorias
def tela_categoria(categoria):
    janela_categoria = tk.Toplevel()
    janela_categoria.title(f"{categoria}")
    janela_categoria.geometry("800x600")

    lbl_categoria = tk.Label(janela_categoria, text=f"{categoria}", font=("Helvetica", 20, "bold"), fg="#000000")
    lbl_categoria.pack(pady=20)

    produtos = {
        "Entradas": ["Salada", "Sopa", "Bruschetta", "Carpaccio", "Ceviche"],
        "Pratos Principais": ["Risoto", "Pasta", "Filet Mignon", "Salmão", "Lasanha"],
        "Bebidas": ["Refrigerante", "Suco", "Água", "Chá Gelado", "Café"],
        "Bebidas Alcoólicas": ["Vinho", "Cerveja", "Whisky", "Caipirinha", "Gin Tônica"],
        "Sobremesas": ["Pudim", "Sorvete", "Petit Gâteau", "Cheesecake", "Tiramisu"],
        "Menu do Chef": ["Especial 1", "Especial 2", "Especial 3", "Especial 4", "Especial 5"]
    }

    card_frame = tk.Frame(janela_categoria)
    card_frame.pack(pady=20)

    for produto in produtos[categoria]:
        frame_produto = tk.Frame(card_frame)
        frame_produto.pack(pady=5, padx=20, fill=tk.X)

        # Imagem do produto em PNG redimensionada
        img_path = f"imagens\{produto.lower().replace(' ', '_')}.png"  
        img = carregar_imagem(img_path)
        if img:
            lbl_img = tk.Label(frame_produto, image=img)
            lbl_img.image = img  
            lbl_img.pack(side=tk.LEFT, padx=10)
        else:
            lbl_img = tk.Label(frame_produto, text="[Imagem]")
            lbl_img.pack(side=tk.LEFT, padx=10)

        btn_produto = ttk.Button(frame_produto, text=produto, style="TButton",
                                 command=lambda p=produto: adicionar_ao_pedido(p))
        btn_produto.pack(side=tk.LEFT, padx=10)

    btn_finalizar = ttk.Button(card_frame, text="Finalizar Pedido", style="TButton", command=visualizar_carrinho)
    btn_finalizar.pack(pady=20)

    janela_categoria.mainloop()

# Função para adicionar ao pedido
carrinho = []

def adicionar_ao_pedido(produto):
    carrinho.append(produto)
    messagebox.showinfo("Adicionado", f"{produto} foi adicionado ao seu pedido.")

# Função para visualizar o carrinho
def visualizar_carrinho():
    janela_carrinho = tk.Toplevel()
    janela_carrinho.title("Carrinho")
    janela_carrinho.geometry("800x600")

    lbl_carrinho = tk.Label(janela_carrinho, text="Seu Carrinho:", font=("Helvetica", 20, "bold"), fg="#000000")
    lbl_carrinho.pack(pady=20)

    frame_itens = tk.Frame(janela_carrinho)
    frame_itens.pack(pady=10)

    for idx, item in enumerate(carrinho, start=1):
        lbl_item = tk.Label(frame_itens, text=f"{idx}. {item}", font=("Helvetica", 14), fg="#000000")
        lbl_item.pack(anchor='w', padx=20, pady=2)

    btn_confirmar = ttk.Button(janela_carrinho, text="Confirmar Pedido", style="TButton", command=finalizar_pedido)
    btn_confirmar.pack(pady=20)

    btn_acrescentar = ttk.Button(janela_carrinho, text="Acrescentar Mais Itens", style="TButton",
                                 command=janela_carrinho.destroy)
    btn_acrescentar.pack(pady=10)

    janela_carrinho.mainloop()

# Função para finalizar o pedido
def finalizar_pedido():
    messagebox.showinfo("Pedido Enviado", "Seu pedido foi enviado à cozinha!")
    janela_finalizacao = tk.Toplevel()
    janela_finalizacao.title("Pedido Finalizado")
    janela_finalizacao.geometry("800x600")

    lbl_final = tk.Label(janela_finalizacao, text="Obrigado pelo seu pedido!", font=("Helvetica", 24, "bold"), fg="#000000")
    lbl_final.pack(pady=20)

    img_divertida = carregar_imagem("imagens/divertida.png")  
    if img_divertida:
        lbl_img = tk.Label(janela_finalizacao, image=img_divertida)
        lbl_img.image = img_divertida  
        lbl_img.pack(pady=10)
    else:
        lbl_img = tk.Label(janela_finalizacao, text="[Imagem Divertida]")
        lbl_img.pack(pady=10)

    btn_sair = ttk.Button(janela_finalizacao, text="Sair", style="TButton", command=janela_finalizacao.quit)
    btn_sair.pack(pady=20)

    janela_finalizacao.mainloop()

# Tela de login
janela_login = tk.Tk()
janela_login.title("Login")
janela_login.geometry("400x400")  

bg_image = carregar_imagem("imagens/fundo_transparente.png")
if bg_image:
    bg_label = tk.Label(janela_login, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(relwidth=1, relheight=1)
else:
    print("Erro ao carregar a imagem de fundo.")

# Usuário
lbl_usuario = tk.Label(janela_login, text="Usuário:", font=("Helvetica", 14), fg="#000000")
lbl_usuario.pack(pady=10)
entry_usuario = tk.Entry(janela_login, font=("Helvetica", 14))
entry_usuario.pack(pady=5)

# Senha
lbl_senha = tk.Label(janela_login, text="Senha:", font=("Helvetica", 14), fg="#000000")
lbl_senha.pack(pady=10)
entry_senha = tk.Entry(janela_login, font=("Helvetica", 14), show="*")
entry_senha.pack(pady=5)

# Confirmar Senha
lbl_confirmar_senha = tk.Label(janela_login, text="Confirmar Senha:", font=("Helvetica", 14), fg="#000000")
lbl_confirmar_senha.pack(pady=10)
entry_confirmar_senha = tk.Entry(janela_login, font=("Helvetica", 14), show="*")
entry_confirmar_senha.pack(pady=5)

# Botão de Login
btn_login = ttk.Button(janela_login, text="Login", command=login)
btn_login.pack(pady=20)

janela_login.mainloop()
