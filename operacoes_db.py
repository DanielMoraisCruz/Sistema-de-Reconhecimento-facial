import sqlite3

from usuario.user import User

# create a connection to the database
db = sqlite3.connect("./database/database.db")


def verifica_user(user) -> bool:
    """Verifica se o usuário já está cadastrado no banco de dados"""
    email = user.email
    cpf = user.cpf

    cursor = db.cursor()
    comando = "SELECT * FROM usuarios WHERE email = ? OR cpf = ?"
    cursor.execute(comando, (email, cpf))
    result = cursor.fetchall()
    if result:
        return True
    else:
        return False


def add_user(user: User):
    if verifica_user(user):
        return "Usuário já cadastrado"

    cursor = db.cursor()
    infos = user.return_infos()
    print(infos)
    comando = (
        f'INSERT INTO usuarios '
        f'VALUES ("{infos["cpf"]}", "{infos["email"]}", '
        f'"{infos["password"]}", "{infos["nivel_acesso"]}", '
        f'"{infos["img"]}")'
    )
    cursor.execute(comando)
    db.commit()

    return "Usuário adicionado com sucesso"


def edit_user(user: User):
    if not (verifica_user(user)):
        return "Usuário não encontrado"

    cursor = db.cursor()
    infos = user.return_infos()
    comando = (
        f'UPDATE usuarios SET email = "{infos["email"]}", '
        f'password = "{infos["password"]}", '
        f'nivel_acesso = "{infos["nivel_acesso"]}", '
        f'img = "{infos["img"]}" WHERE cpf = "{infos["cpf"]}"'
    )
    cursor.execute(comando)
    db.commit()

    return "Usuário editado com sucesso"


def delet_user(user: User):
    if not (verifica_user(user)):
        return "Usuário não encontrado"

    cursor = db.cursor()
    comando = f'DELETE FROM usuarios WHERE cpf = "{user.cpf}"'
    cursor.execute(comando)
    db.commit()

    return "Usuário deletado com sucesso"


def get_user(user: User = None):
    cursor = db.cursor()
    if not (user is None):
        if not (verifica_user(user)):
            return "Usuário não encontrado"

        comando = f'SELECT * FROM usuarios WHERE cpf = "{user.cpf}"'
    else:
        comando = 'SELECT * FROM usuarios'

    cursor.execute(comando)
    result = cursor.fetchall()

    return result


def valida_senha_usuario(user: User):
    cursor = db.cursor()
    comando = f'SELECT password FROM usuarios WHERE cpf = "{user.cpf}"'
    cursor.execute(comando)
    result = cursor.fetchall()
    print(result)

    # if result == user.password:
    #     return True
    # else:
    #     return False


if __name__ == "__main__":
    user: User = User(
        email="daniel.jack.dmc@gmail.com",
        password="1234567-",
        cpf="960.013.722-68",
        img="daniel.jpg",
        nivel_acess=3
    )

    # print(add_user(user))
    print(valida_senha_usuario(user))
    # print(edit_user(user))
    # print(delet_user(user))
