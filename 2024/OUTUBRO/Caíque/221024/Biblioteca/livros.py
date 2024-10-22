class livro:
    def __init__ (self,titulo,autor,emprestimo=False):
        self.titulo = titulo
        self.autor = autor
        self.emprestimo = emprestimo

class biblioteca:
    def disponivel(self):
        livro == disponivel


class usuario:
    def __init__(self,nome,data):
        self.nome = nome
        self.data = data

        
# Classe Livro
# class Livro:
#     def __init__(self, titulo, autor, emprestimo=False):
#         self.titulo = titulo
#         self.autor = autor
#         self.emprestimo = emprestimo
    
#     def emprestar(self):
#         if not self.emprestimo:
#             self.emprestimo = True
#             print(f"O livro '{self.titulo}' foi emprestado.")
#         else:
#             print(f"O livro '{self.titulo}' já está emprestado.")
    
# # Classe Usuario
# class Usuario:
#     def __init__(self, nome, data_cadastro):
#         self.nome = nome
#         self.data_cadastro = data_cadastro
#         self.livros_emprestados = []
    
#     def pegar_emprestado(self, livro):
#         if not livro.emprestimo:
#             livro.emprestar()
#             self.livros_emprestados.append(livro)
#             print(f"{self.nome} emprestou o livro '{livro.titulo}'.")
#         else:
#             print(f"{self.nome} não pode pegar o livro '{livro.titulo}' pois ele já está emprestado.")

# # Exemplo de uso
# if __name__ == "__main__":
#     # Criando livros
#     livro1 = Livro("1984", "George Orwell")
#     livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")

#     # Criando um usuário
#     usuario1 = Usuario("Davi", "22/10/2024")
    
#     # Emprestando livros
#     usuario1.pegar_emprestado(livro1)
#     usuario1.pegar_emprestado(livro2)
    
