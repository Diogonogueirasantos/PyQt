import mysql.connector
import getpass


class database_maneger:
    def __init__(self):
        self.database_conection()
        self.create_user()

    def database_conection(self):
        user = getpass.getpass(prompt="Por favor insira seu nome de usuário: ")
        password_user = getpass.getpass(prompt='Insira sua senha por favor: ')
        self.database_cursor = mysql.connector.connect(user=f'{user}', password=f'{password_user}',
                                                       host='localhost',
                                                       database='clientes')

        if self.database_cursor.is_connected():
            print('Conexão estabelecida!')
        else:
            print('Parece que houve um erro ao estabelecer a conexão com seu banco de dados.', end=" ")
            print('Tente novamente!')

    def create_user(self):
        self.database_cursor.cursor()


Instanciador = database_maneger()
Instanciador.create_user()
