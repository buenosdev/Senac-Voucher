from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.uic import loadUi


class CadastroLiUser(QMainWindow):
    def __init__(self, stack):
        super().__init__()
        loadUi('Views/cadastro_li_user.ui', self)
        self.stack = stack

        # Configuração dos botões
        self.btnCad_Livro.clicked.connect(lambda: stack.setCurrentIndex(3))  # Cadastro Livro
        self.btnCad_User.clicked.connect(lambda: stack.setCurrentIndex(1))  # Cadastro User
        self.btnEmprestimo.clicked.connect(lambda: stack.setCurrentIndex(5))  # Empréstimo Livro


class CadastroUser(QMainWindow):
    def __init__(self, stack):
        super().__init__()
        loadUi('Views/cadastro_user.ui', self)
        self.stack = stack

        # Configuração do botão
        self.btnSalvar.clicked.connect(lambda: stack.setCurrentIndex(0))  # Voltar para CadastroLiUser


class CadastroAdmin(QMainWindow):
    def __init__(self, stack):
        super().__init__()
        loadUi('Views/cadastro_admin.ui', self)
        self.stack = stack

        # Configuração do botão
        self.btnSalvar.clicked.connect(lambda: stack.setCurrentIndex(4))  # Voltar para Login


class CadastroLivro(QMainWindow):
    def __init__(self, stack):
        super().__init__()
        loadUi('Views/cadastro_livro.ui', self)
        self.stack = stack

        # Configuração do botão
        self.btnSalvar.clicked.connect(lambda: print("Livro cadastrado com sucesso!"))


class Login(QMainWindow):
    def __init__(self, stack):
        super().__init__()
        loadUi('Views/login.ui', self)
        self.stack = stack

        # Configuração dos botões
        self.btnEntrar.clicked.connect(lambda: stack.setCurrentIndex(0))  # Ir para CadastroLiUser
        self.btnCadastrar.clicked.connect(lambda: stack.setCurrentIndex(2))  # Ir para CadastroAdmin


class EmprestimoLivro(QMainWindow):
    def __init__(self, stack):
        super().__init__()
        loadUi('Views/emprestimo_livro.ui', self)
        self.stack = stack

        # Configuração do botão
        self.btnSalvar.clicked.connect(lambda: print("Empréstimo realizado!"))


class BibliotecaApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Adicionando as telas ao stack
        self.cadastro_li_user = CadastroLiUser(self)
        self.cadastro_user = CadastroUser(self)
        self.cadastro_admin = CadastroAdmin(self)
        self.cadastro_livro = CadastroLivro(self)
        self.login = Login(self)
        self.emprestimo_livro = EmprestimoLivro(self)

        self.addWidget(self.cadastro_li_user)  # Índice 0
        self.addWidget(self.cadastro_user)    # Índice 1
        self.addWidget(self.cadastro_admin)  # Índice 2
        self.addWidget(self.cadastro_livro)  # Índice 3
        self.addWidget(self.login)           # Índice 4
        self.addWidget(self.emprestimo_livro)  # Índice 5
