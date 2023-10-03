from flask import Flask  # , Response, render_template

app = Flask(__name__)

# login |email e senha|
# cadastro |email, senha, cpf, foto em base64|


@app.route('/api_v1')
def login():
    return 'login'


if __name__ == '__main__':
    app.run(debug=True)
