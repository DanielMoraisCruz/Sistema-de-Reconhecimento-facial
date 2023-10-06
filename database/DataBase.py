import sqlite3

from usuario.user import User

# create a connection to the database
db = sqlite3.connect('database.db')


def verifica_user(user) -> bool:
    '''Verifica se o usuário já está cadastrado no banco de dados'''
    email = user.email
    cpf = user.cpf

    cursor = db.cursor()
    comando = "SELECT * FROM usuarios WHERE email = ? OR cpf = ?"
    cursor.execute(comando, (email, cpf))
    result = cursor.fetchall()
    if result:
        return False
    else:
        return True


def add_user(user: User, nivel_acesso: int = 0):
    if verifica_user(user):
        return 'Usuário já cadastrado'

    cursor = db.cursor()
    infos = user.return_infos(nivel_acesso)
    comando = (
        f"INSERT INTO usuarios "
        f"VALUES ('{infos['email']}', '{infos['password']}', "
        f"'{infos['cpf']}', '{infos['img']}', '{infos['token']}', "
        f"{infos['nivel_acesso']})"
    )
    cursor.execute(comando)
    db.commit()

    return 'Usuário adicionado com sucesso'


def edit_user(user: User, nivel_acesso: int = 0):
    if not (verifica_user(user)):
        return 'Usuário não encontrado'

    cursor = db.cursor()
    infos = user.return_infos(nivel_acesso)
    comando = (
        f"UPDATE usuarios SET email = '{infos['email']}', "
        f"password = '{infos['password']}', cpf = '{infos['cpf']}', "
        f"img = '{infos['img']}', token = '{infos['token']}', "
        f"nivel_acesso = {infos['nivel_acesso']} "
        f"WHERE cpf = '{infos['cpf']}'"
    )
    cursor.execute(comando)
    db.commit()

    return 'Usuário editado com sucesso'


def delet_user(user: User):
    if not (verifica_user(user)):
        return 'Usuário não encontrado'

    cursor = db.cursor()
    comando = f"DELETE FROM usuarios WHERE cpf = '{user.cpf}'"
    cursor.execute(comando)
    db.commit()

    return 'Usuário deletado com sucesso'


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
