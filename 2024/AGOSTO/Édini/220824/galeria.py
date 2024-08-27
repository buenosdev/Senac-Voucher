import tkinter as tk
from tkinter import PhotoImage, messagebox

class GalleryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Galeria de Arte")
        
        # Lista de imagens para a galeria
        self.images = [
            PhotoImage(file="meme1.png"),
            PhotoImage(file="meme2.png"),
            PhotoImage(file="meme3.png")
        ]
        self.index = 0  
        
        self.setup_ui()
        self.show_image(self.index)
    
    def setup_ui(self):
        self.background_image = PhotoImage(file="background.png")  
        self.bg_label = tk.Label(self.root, image=self.background_image)
        self.bg_label.place(relwidth=1, relheight=1)  
        
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=20)
        
        nav_frame = tk.Frame(self.root, bg="lightgray")  
        nav_frame.pack(pady=10)
        
        self.prev_button = tk.Button(nav_frame, text="<", command=self.prev_image)
        self.prev_button.pack(side=tk.LEFT)
        
        self.next_button = tk.Button(nav_frame, text=">", command=self.next_image)
        self.next_button.pack(side=tk.LEFT)

        self.desc_label = tk.Label(self.root, text="Descrição:", bg="lightgray")
        self.desc_label.pack()
        
        self.desc_entry = tk.Entry(self.root, width=50)
        self.desc_entry.pack(pady=5)
        
        self.save_button = tk.Button(self.root, text="Salvar Descrição", command=self.save_description)
        self.save_button.pack(pady=10)
    
    def show_image(self, index):
        if 0 <= index < len(self.images):
            img = self.images[index]
            self.image_label.config(image=img)
            self.image_label.image = img
            self.index = index
    
    def prev_image(self):
        if self.images:
            new_index = (self.index - 1) % len(self.images)
            self.show_image(new_index)
    
    def next_image(self):
        if self.images:
            new_index = (self.index + 1) % len(self.images)
            self.show_image(new_index)
    
    def save_description(self):
        desc = self.desc_entry.get()
        if desc:
            print(f"Descrição para imagem {self.index + 1}: {desc}")
            messagebox.showinfo("Descrição Salva", "Descrição salva com sucesso!")
        else:
            messagebox.showwarning("Descrição Vazia", "A descrição não pode estar vazia.")

root = tk.Tk()
app = GalleryApp(root)
root.mainloop()
