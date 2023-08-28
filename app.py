from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('acesso.html')

@app.route('/cadastro')
def cadastro():
  return render_template('cadastro.html')

@app.route('/competicoes')
def competicoes():
  return render_template('competicoes.html')


app.run(host='0.0.0.0', port=81)