import random

ADMIN = 3
USER = 2
GUEST = 1


class User(object):
    def __init__(self, email: str = '', password: str = '',
                 cpf: str = '', img: str = '',
                 token: str = '', nivel_acess: int = 0) -> None:
        self.email = email
        self.password = password
        self.cpf = cpf
        self.img = img
        self.token = token
        self.nivel_acesso = nivel_acess

    def generate_token(self) -> str:
        num = random.randint(1000, 9999)
        self.token = f"{self.infos['cpf']}{num}"
        return self.token

    def return_infos(self, nivel) -> dict:
        '''Retorna as informações do usuário de acordo com o nível de acesso'''

        self.infos: dict = {}
        if nivel >= GUEST:
            self.infos['email'] = self.email
        if nivel >= USER:
            self.infos['nivel_acesso'] = self.nivel_acesso
        if nivel >= ADMIN:
            self.infos['cpf'] = self.cpf
            self.infos['token'] = self.token
            self.infos['password'] = self.password
            self.infos['img'] = self.img

        return self.infos


if __name__ == '__main__':
    user = User()
    infos_user = user.return_infos(ADMIN)
    print(infos_user)
    infos_user = user.return_infos(USER)
    print(infos_user)
    infos_user = user.return_infos(GUEST)
    print(infos_user)
