import random


class User(object):
    def __init__(self) -> None:
        self.infos: dict = {
            'email': '',
            'password': '',
            'cpf': 'teste',
            'img': '',
            'nivel_acesso': 0,
            'token': ''
        }

    def generate_token(self) -> str:
        num = random.randint(1000, 9999)
        self.infos['token'] = f"""{self.infos['cpf']}{num}"""
        return self.infos['token']
