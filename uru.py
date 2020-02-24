from flask import Flask, render_template

# ...

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/clientes')
def clientes():
    return render_template('lista_clientes.html')
