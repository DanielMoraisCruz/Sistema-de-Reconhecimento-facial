import random

import bcrypt

NIVEL3 = 3
NIVEL2 = 2
NIVEL1 = 1


class User(object):
    def __init__(self, email: str, password: str, cpf: str, img: str = '',
                 nivel_acess: int = 0) -> None:
        self.email = email
        self.password = self.senha_criptografada(password)
        self.cpf = self.trata_cpf(cpf)
        self.img = img
        self.nivel_acesso = nivel_acess
        self.infos: dict = {}

        self.token = ''
        self.generate_token()

    def generate_token(self) -> str:
        num = random.randint(1000, 9999)
        self.token = f"{self.cpf}{num}"

    def return_infos(self) -> dict:
        '''Retorna as informações do usuário de acordo com o nível de acesso'''

        self.infos['email'] = self.email
        self.infos['nivel_acesso'] = self.nivel_acesso
        self.infos['cpf'] = self.cpf
        self.infos['token'] = self.token
        self.infos['password'] = self.password
        self.infos['img'] = self.img

        return self.infos

    def trata_cpf(self, cpf: str) -> str:
        '''Trata o cpf para ser armazenado no banco de dados'''
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
        return cpf

    def senha_criptografada(self, senha: str):
        return f"{bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())}"

    def verifica_senha(self, senha: str):
        return bcrypt.checkpw(senha.encode('utf-8'), self.password)


if __name__ == '__main__':
    user = User()
    infos_user = user.return_infos(NIVEL3)
    print(infos_user)
