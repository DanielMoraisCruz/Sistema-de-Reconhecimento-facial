import sqlite3

from usuario.user import User

# create a connection to the database


def verifica_user(user) -> bool:
    """Verifica se o usuário já está cadastrado no banco de dados"""
    db = sqlite3.connect("./database/database.db")
    email = user.email
    cpf = user.cpf

    cursor = db.cursor()
    comando = "SELECT * FROM usuarios WHERE email = ? OR cpf = ?"
    cursor.execute(comando, (email, cpf))
    result = cursor.fetchall()
    if result:
        print('ususario ja cadastrado')
        return True
    else:
        print('ususario ja cadastrado')
        return False


def add_user(user: User):
    db = sqlite3.connect("./database/database.db")
    if verifica_user(user):
        return "Usuário já cadastrado"

    cursor = db.cursor()
    infos = user.return_infos(pw=True)
    print(infos)
    comando = "INSERT INTO usuarios VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(comando, (
        infos["cpf"],
        infos["email"],
        infos["password"],
        infos["nivel_acesso"],
        infos["image"],
        infos["token"]
    ))
    db.commit()

    return "Usuário adicionado com sucesso"


def delet_user(user: User):
    db = sqlite3.connect("./database/database.db")
    if not (verifica_user(user)):
        return "Usuário não encontrado"

    cursor = db.cursor()
    comando = 'DELETE FROM usuarios WHERE cpf = ?'
    cursor.execute(comando, [user.cpf])
    db.commit()

    return "Usuário deletado com sucesso"


def get_user(user: User = None):
    db = sqlite3.connect("./database/database.db")
    cursor = db.cursor()
    if not (user is None):
        if not (verifica_user(user)):
            return "Usuário não encontrado"

        comando = """SELECT email, password, cpf, img, nivel_acesso
                     FROM usuarios WHERE email = ?"""
        cursor.execute(comando, [user.email])
    else:
        comando = "SELECT * FROM usuarios"
        cursor.execute(comando)
    result = cursor.fetchall()
    print(result)

    return result


def valida_senha_usuario(user: User):
    db = sqlite3.connect("./database/database.db")
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
        password="1234567",
        cpf="960.013.722-68",
        image="daniel.jpg",
        nivel_acess=3
    )

    print(add_user(user))
    # print(valida_senha_usuario(user))
    # print(edit_user(user))
    # print(delet_user(user))
