
import random

import bcrypt

NIVEL3 = 3
NIVEL2 = 2
NIVEL1 = 1


class User(object):

    def __init__(self, email: str = '', password: str = '', cpf: str = '',
                 image: str = '', nivel_acess: int = 0) -> None:
        self.email = email
        self.password = self.senha_criptografada(password)
        self.cpf = self.trata_cpf(cpf)
        self.image = image
        self.nivel_acesso = nivel_acess
        self.infos: dict = {}

        self.token = ''
        self.generate_token()

    def generate_token(self):
        num = random.randint(1000, 9999)
        self.token = f"{self.cpf}{num}"

    def return_infos(self, pw: bool = False) -> dict:
        '''Retorna as informações do usuário de acordo com o nível de acesso'''

        self.infos['email'] = self.email
        self.infos['nivel_acesso'] = self.nivel_acesso
        self.infos['cpf'] = self.cpf
        self.infos['token'] = self.token
        self.infos['password'] = self.password if pw else None
        self.infos['image'] = self.image

        return self.infos

    def trata_cpf(self, cpf: str) -> str:
        '''Trata o cpf para ser armazenado no banco de dados'''
        cpf = cpf.replace('.', '').replace('-', '')
        return cpf

    def senha_criptografada(self, senha: str):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def verifica_senha(self, senha: str):
        return bcrypt.checkpw(senha.encode('utf-8'),
                              self.password.encode('utf-8'))

    @staticmethod
    def criar_login(login):
        email: str = login['email']
        password: str = login['password']
        image: str = login['image']
        return User(email, password, image=image)

    @staticmethod
    def criar_user(user):
        email: str = user['email']
        password: str = user['password']
        cpf: str = user['cpf']
        image: str = user['image']
        nivel: int = user['nivel']
        return User(email, password, cpf, image, nivel)


if __name__ == '__main__':
    user = User()
    infos_user = user.return_infos()
    print(infos_user)
