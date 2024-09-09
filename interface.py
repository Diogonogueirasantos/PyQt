import sys
from PyQt6.QtWidgets import QApplication, QWidget


class janela_principal(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciadorUI()

    def iniciadorUI(self):
        self.setGeometry(200, 100, 400, 300)  # (x=200, y=100, l=400, a=300)
        self.setWindowTitle('Minha primeira UI')
        self.show()


if __name__ == '__main__': # permite com que o código não se inicie automaticamente.
    app = QApplication(sys.argv)
    instanciador = janela_principal()
    sys.exit(app.exec())
