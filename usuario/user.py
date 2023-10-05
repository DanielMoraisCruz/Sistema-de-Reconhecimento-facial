import random

NIVEL3 = 3
NIVEL2 = 2
NIVEL1 = 1


class User(object):
    def __init__(self, email: str, password: str, cpf: str, img: str = '',
                 nivel_acess: int = 0) -> None:
        self.email = email
        self.password = password
        self.cpf = cpf
        self.img = img
        self.token = ''
        self.generate_token()
        self.nivel_acesso = nivel_acess
        self.infos: dict = {}

    def generate_token(self) -> str:
        num = random.randint(1000, 9999)
        self.token = f"{self.infos['cpf']}{num}"
        return self.token

    def return_infos(self, nivel) -> dict:
        '''Retorna as informações do usuário de acordo com o nível de acesso'''

        self.infos['email'] = self.email
        self.infos['nivel_acesso'] = self.nivel_acesso
        self.infos['cpf'] = self.cpf
        self.infos['token'] = self.token
        self.infos['password'] = self.password
        self.infos['img'] = self.img

        return self.infos


if __name__ == '__main__':
    user = User()
    infos_user = user.return_infos(NIVEL3)
    print(infos_user)
