from flask import Flask, Response, jsonify, request  # , abort
from flask_cors import CORS

from operacoes_db import get_one_user  # add_user, delet_user, get_user,
from operacoes_db import user_existe
from recog_face import verifica_rosto
from usuario.user import User

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


@app.route('/admin', methods=['DELETE'])
def delete_user():
    return jsonify('DELETE USER')


@app.route('/admin', methods=['PATCH'])
def mudar_nivel_acesso():
    return jsonify('PATCH USER')


def resource_not_found(message: str) -> Response:
    error_message = {"message": message}
    response = jsonify(error_message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)
