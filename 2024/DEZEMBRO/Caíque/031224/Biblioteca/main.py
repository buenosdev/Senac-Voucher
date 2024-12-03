import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from biblioteca import BibliotecaApp


def main():
    app = QApplication(sys.argv)
    main_app = BibliotecaApp()
    main_app.setCurrentIndex(4)  # Inicia com a tela de login
    main_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
