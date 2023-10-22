from flask import Flask, Response, jsonify, request
from flask_cors import CORS

from operacoes_db import (add_user, checar_nivel, delet_user, get_one_user,
                          user_existe)
from face_recog import verifica_rosto
from user import User

app = Flask(__name__)
app.config['JASON_SORT_KEYS'] = False
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    # Recebe os dados do login
    user: User = User.criar_login(request.get_json())

    # Validação por IA do login
    cred_invalid_error = 'Credenciais Invalidas'
    if not user_existe(user):
        return resource_not_found(cred_invalid_error)

    if not verifica_rosto(user):
        return resource_not_found(cred_invalid_error)

    persisted_user = get_one_user(user)
    user = User(persisted_user[0], persisted_user[1],
                persisted_user[2], persisted_user[3], persisted_user[4])

    return jsonify(user.return_infos())


@app.route('/cadastro', methods=['POST'])
def cadastrar_user():
    user: User = User.criar_user(request.get_json())

    if user_existe(user):
        return resource_not_found('Usuário já cadastrado')

    try:
        add_user(user)
    except Exception as e:
        return resource_not_found('Erro ao cadastrar usuário ' + str(e))
    return jsonify(user.return_infos())


@app.route('/deletar', methods=['DELETE'])
def delete_user():
    user: User = User.criar_user(request.get_json())
    if not user_existe(user):
        return resource_not_found('Usuário não encontrado')
    try:
        delet_user(user)
    except Exception as e:
        return resource_not_found('Erro ao deletar usuário ' + str(e))
    return custom_response('Usuário deletado com sucesso', 200)


@app.route('/check-access/<nivel>/<email>', methods=['GET'])
def check_nivel(nivel, email):
    user: User = User(email)
    message, status = checar_nivel(user, nivel)
    return custom_response(message, status)


def resource_not_found(message: str) -> Response:
    error_message = {"message": message}
    response = jsonify(error_message)
    response.status_code = 404
    return response


def custom_response(message: str, status: int) -> Response:
    error_message = {"message": message}
    response = jsonify(error_message)
    response.status_code = status
    return response


if __name__ == '__main__':
    app.run(debug=True)
