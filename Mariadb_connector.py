import mysql.connector
import getpass


class database_Connector:
    def __init__(self):
        self.database_Conection()

    def database_Conection(self):
        user = getpass.getpass(prompt='Insira o seu nome de usuário: ')
        password = getpass.getpass(prompt='Insira sua senha: ')
        self.cursor = mysql.connector.connect(user=f'{user}', password=f'{password}',
                                              host='localhost', database='clientes')
        try:
            self.cursor.is_connected()
        except ValueError:
            print('Usuario ou senha incorretos!')

    def teste(self):
        print('Olá, mundo!')
