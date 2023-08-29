from flask import Flask , render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('acesso.html')

@app.route('/home')
def visitante():
  return render_template('home.html')

@app.route('/visitante')
def visitante():
  return render_template('visitante.html')

@app.route('/usuario', methods=['POST'])
def usuario():
  return render_template('usuario.html')

@app.route('/home', methods=['POST'])
def home():
  n=request.form['nome']
  m=request.form['matricula']
  s=request.form['senha']
  return render_template('home.html', n=n, m=m,s=s)

@app.route('/cadastro')
def cadastro():
  return render_template('cadastro.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
  n=request.form['nome']
  g=request.form['grupo']
  e=request.form['email']
  m=request.form['matricula']
  s=request.form['senha']
  return render_template('usuario.html',n=n, g=g, e=e, m=m, s=s)

@app.route('/modalidades')
def modalidades():
  return render_template('modalidades.html')

@app.route('/modalidades_esportivas')
def modalidades_esportivas():
  return render_template('modesportes.html')

@app.route('/modalidades_culturais')
def modalidades_culturais():
  return render_template('modcultural.html')

@app.route('/torcida')
def torcida():
  return render_template('torcida.html')

@app.route('/pontuacao')
def pontuacao():
  return render_template('pontuacao.html')

@app.route('/faq')
def faq():
  return render_template('faq.html')

@app.route('/competicoes')
def competicoes():
  return render_template('competicoes.html')

app.run(host='0.0.0.0', port=81)