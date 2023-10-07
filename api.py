from flask import Flask, jsonify, request
from flask_cors import CORS

from operacoes_db import (add_user, delet_user, edit_user, get_user,
                          verifica_user)
from usuario.user import User

app = Flask(__name__)
app.config['JASON_SORT_KEYS'] = False
CORS(app)


def valid_login(user: User):
    if not (verifica_user(user)):
        return False
    # Validação por IA do login


@app.route('/login', methods=['POST'])
def login():
    # Recebe os dados do login
    user: User = User()
    # verifica se o usuário existe no banco

    data = request.get_json()
    user.infos = user.return_infos(3)

    user.infos['email'] = data['email']
    user.infos['password'] = data['password']
    user.infos['img'] = data['img']

    # Validação por IA do login
    if not valid_login(user):
        return 'Usuário não encontrado', 404

    token = user.generate_token()
    user.infos['token'] = token

    return user.infos, 200


@app.route('/users', methods=['GET'])
def get_users():
    # Checa se o usuário está logado
    # Checa o nivel de acesso do usuário
    # Se for admin, retorna todos os usuários
    # Se não for admin, retorna apenas o usuário logado

    return jsonify('GET ALL USERS')


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    # Checa se o usuário está logado
    # Checa o nivel de acesso do usuário
    # Checa se o usuário existe
    # Se existir, retorna o usuário
    # Se não existir, retorna erro

    return jsonify(f'GET USER {id}')


@app.route('/users', methods=['POST'])
def post_user():
    # Checa se o usuário está logado
    # Checa o nivel de acesso do usuário
    # Checa se o usuário existe
    # Se existir, retorna erro
    # Se não existir, cria o usuário

    return jsonify('POST USER')


@app.route('/users/<int:id>', methods=['PUT'])
def put_user(id):
    # Checa se o usuário está logado
    # Checa o nivel de acesso do usuário
    # Checa se o usuário existe
    # Se existir, verifica se o usuário tem permissão para editar
    # Se tiver, edita
    # Se não existir, retorna erro

    return jsonify(f'PUT USER {id}')


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Checa se o usuário está logado
    # Checa o nivel de acesso do usuário
    # Checa se o usuário existe
    # Se existir, verifica se o usuário tem permissão para deletar
    # Se tiver, deleta
    # Se não existir, retorna erro

    return jsonify(f'DELETE USER {id}')


if __name__ == '__main__':
    app.run(debug=True)
