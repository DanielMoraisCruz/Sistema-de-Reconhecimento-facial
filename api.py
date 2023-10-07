from flask import Flask, jsonify, request
from flask_cors import CORS

from operacoes_db import add_user, delet_user, get_user, verifica_user
from usuario.user import User

app = Flask(__name__)
app.config['JASON_SORT_KEYS'] = False
CORS(app)


def validacao_por_IA(user: User):
    return True
    # Validação por IA do login


@app.route('/login', methods=['POST'])
def login():
    # Recebe os dados do login
    user: User = User.criar_login(request.get_json())

    # Validação por IA do login
    if not (verifica_user(user) or validacao_por_IA(user)):
        return 'Credenciais Invalidas', 404

    usuario = get_user(user)[0]
    print(usuario)
    user = User(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4])

    return jsonify(user.return_infos())


@app.route('/admin', methods=['DELETE'])
def delete_user():
    return jsonify('DELETE USER')


@app.route('/admin', methods=['PATCH'])
def mudar_nivel_acesso():
    return jsonify('PATCH USER')


if __name__ == '__main__':
    app.run(debug=True)
