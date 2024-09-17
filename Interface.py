from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import sys
import Mariadb_connector
import Wallet


class InicializationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.InterfaceUI()

    def InterfaceUI(self):
        self.setGeometry(665, 435, 800, 750)
        self.setWindowTitle('Your Money')
        self.Bottons()
        self.show()

    def Bottons(self):
        self.clique = QPushButton('Clique aqui!', self)
        self.clique.clicked.connect(Mariadb_connector.database_Connector.teste)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = InicializationUI()
    app.exec()

