import sqlite3

from usuario.user import User

# create a connection to the database


def user_existe(user) -> bool:
    """Verifica se o usuário já está cadastrado no banco de dados"""
    db = connect_to_db()
    email = user.email
    cpf = user.cpf

    cursor = db.cursor()
    comando = "SELECT * FROM usuarios WHERE email = ? OR cpf = ?"
    cursor.execute(comando, (email, cpf))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def add_user(user: User):
    db = connect_to_db()
    if user_existe(user):
        return "Usuário já cadastrado"

    cursor = db.cursor()
    infos = user.return_infos(pw=True)
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
    db = connect_to_db()
    if not (user_existe(user)):
        return "Usuário não encontrado"

    cursor = db.cursor()
    comando = 'DELETE FROM usuarios WHERE cpf = ?'
    cursor.execute(comando, [user.cpf])
    db.commit()

    return "Usuário deletado com sucesso"


def get_user(user: User = None):
    db = connect_to_db()
    cursor = db.cursor()
    if not (user is None):
        if not (user_existe(user)):
            return "Usuário não encontrado"

        comando = """SELECT email, password, cpf, img, nivel_acesso
                     FROM usuarios WHERE email = ?"""
        cursor.execute(comando, [user.email])
    else:
        comando = "SELECT * FROM usuarios"
        cursor.execute(comando)
    result = cursor.fetchall()

    return result


def get_one_user(user: User = None):
    if not user:
        raise LookupError("User does not exists")
    db = connect_to_db()
    cursor = db.cursor()
    comando = """SELECT email, password, cpf, img, nivel_acesso, token
                 FROM usuarios WHERE email = ?"""
    cursor.execute(comando, [user.email])
    result = cursor.fetchone()
    db.close()
    return result


def valida_senha_usuario(user: User):
    db = connect_to_db()
    cursor = db.cursor()
    comando = 'SELECT password FROM usuarios WHERE cpf = ?'
    cursor.execute(comando, [user.cpf])
    result = cursor.fetchall()
    print(result, 'Ainda não implementado')

    # if result == user.password:
    #     return True
    # else:
    #     return False


def connect_to_db():
    db = sqlite3.connect("./database/database.db")
    return db


if __name__ == "__main__":
    user: User = User(
        email="daniel.jack.dmc@gmail.com",
        password="1234567",
        cpf="960.013.722-68",
        image="daniel.jpg",
        nivel_acess=3
    )
