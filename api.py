from flask import Flask, Response, jsonify, request

from user import User

app = Flask(__name__)
app.config['JASON_SORT_KEYS'] = False

# login |email e senha|
# cadastro |email, senha, cpf, foto em base64|

# CRUD |create, read, update, delete|

usuarios_logado = []


def valid_login(user: User):
    return False


@app.route('/login', methods=['POST'])
def login():
    user: User = User()
    try:
        user['email'] = request.json['email']
        user['password'] = request.json['password']
        user['cpf'] = request.json['cpf']
        user['foto'] = request.json['img']
    except KeyError:
        return Response('Missing parameters', status=400)

    if valid_login(user):
        user['token'] = user.generate_token()
        usuarios_logado.append(user['token'])
        return jsonify(user)
    else:
        return Response('Invalid login', status=401)

    # Checa se o usuário está logado

    # Checa o nivel de acesso do usuário
    # Checa se o usuário existe
    # Se existir, verifica se a senha está correta
    # Se estiver, loga
    # Se não estiver, retorna erro


@app.route('/users', methods=['GET'])
def get_users():
    # Checa se o usuário está logado
    # Checa o nivel de acesso do usuário
    # Se for admin, retorna todos os usuários
    # Se não for admin, retorna apenas o usuário logado

    return Response('GET ALL USERS')


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    # Checa se o usuário está logado
    # Checa o nivel de acesso do usuário
    # Checa se o usuário existe
    # Se existir, retorna o usuário
    # Se não existir, retorna erro

    return Response(f'GET USER {id}')


@app.route('/users', methods=['POST'])
def post_user():
    # Checa se o usuário está logado
    # Checa o nivel de acesso do usuário
    # Checa se o usuário existe
    # Se existir, retorna erro
    # Se não existir, cria o usuário

    return Response('POST USER')


@app.route('/users/<int:id>', methods=['PUT'])
def put_user(id):
    # Checa se o usuário está logado
    # Checa o nivel de acesso do usuário
    # Checa se o usuário existe
    # Se existir, verifica se o usuário tem permissão para editar
    # Se tiver, edita
    # Se não existir, retorna erro

    return Response(f'PUT USER {id}')


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Checa se o usuário está logado
    # Checa o nivel de acesso do usuário
    # Checa se o usuário existe
    # Se existir, verifica se o usuário tem permissão para deletar
    # Se tiver, deleta
    # Se não existir, retorna erro

    return Response(f'DELETE USER {id}')


if __name__ == '__main__':
    app.run(debug=True)
