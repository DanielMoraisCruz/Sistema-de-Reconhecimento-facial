import random


class User(object):
    def __init__(self) -> None:
        self.user: dict = {
            'email': '',
            'password': '',
            'cpf': '',
            'foto': '',
            'nivel_acesso': 0,
            'token': ''
        }

    def generate_token(self) -> str:
        self.user['token'] = f'{self.cpf}{random.randint(1000, 9999)}'
        return self.user['token']
