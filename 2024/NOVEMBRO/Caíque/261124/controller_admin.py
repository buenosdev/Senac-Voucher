class controller_admin:
    @staticmethod
    def cadastrar_livro(titulo):
        livro = livro(titulo)
        banco.connect(livro.create())