
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton
# from controllers.biblioteca import Biblioteca as B
 
# pip install PyQt6
# https://build-system.fman.io/qt-designer-download
 
telaMain = 'Views/main.ui'
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.load_ui.loadUi(telaMain, self)
        self.button.clicked.connect(self.click_cad)
 
    def click_cad(self):
        titulo = self.inputTitulo.text()
        biblioteca.cadastrar_livro(titulo)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



