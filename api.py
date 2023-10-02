from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/reconhecimento')
def reconhecimento():
    return render_template('reconhecimento.html')


@app.route('/photo')
def photo():
    return render_template('photo.html')


@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return jsonify({'msg': 'Hello World!'})
    elif request.method == 'POST':
        return jsonify({'msg': 'Hello World!'})


if __name__ == '__main__':
    app.run(debug=True)
