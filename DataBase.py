import pandas as pd

from usuario.user import User

# data = {
#     'email': ['juquinha123@gmail.com', ' denis.the.row@gmail.com'],
#     'cpf': ['123.456.789-00', '987.654.321-00'],
#     'password': ['123456', '654321'],
#     'img': ['juquinha.jpg', 'denis.jpg'],
#     'token': ['12345678900', '98765432100'],
#     'nivel_acesso': [3, 2]
# }

# df = pd.DataFrame(data)
# df.to_excel('DataBase.xlsx', index=False)

db = pd.read_excel('DataBase.xlsx')


def atualiza_db():
    pass


def busca_user(email: str, cpf: str) -> bool:
    if cpf in db['cpf'] or email in db['email']:
        return True
    else:
        return False


def add_user(user: User, nivel_acesso: int = 0):
    if busca_user(user.email, user.cpf):
        return 'Usuário já cadastrado'
    db.loc[len(db)] = user.return_infos(nivel_acesso)
    atualiza_db()
    return 'Usuário adicionado com sucesso'


def edit_user(user: User, nivel_acesso: int = 0):
    if not (busca_user()):
        db.loc[db['cpf'] == user.cpf] = user.return_infos(nivel_acesso)
        atualiza_db()
        return 'Usuário editado com sucesso'
    else:
        return 'Usuário não encontrado'


def delet_user(user: User):
    if not (busca_user()):
        db.drop(db.loc[db['cpf'] == user.cpf].index, inplace=True)
        atualiza_db()
        return 'Usuário deletado com sucesso'
    else:
        return 'Usuário não encontrado'


if __name__ == '__main__':
    try:
        user = User(
            email='daniel.jack.dmc@gmail.com',
            password='123456',
            cpf='960.013.722-68',
            img='daniel.jpg',
            nivel_acess=3
        )
    except Exception as e:
        print(e)
    else:
        print(add_user(user))
