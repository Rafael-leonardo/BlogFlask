from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "r1s6a2e5f7p1a9e4e8l33l"
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String, nullable=False)
    tempo = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String, nullable=False)

@app.route('/', methods=["GET", "POST"])
def index():
    posts = Post.query.order_by(Post.tempo.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/adicionar', methods=["GET", "POST"])
def adicionar():
    return render_template('adicionar.html')

@app.route('/Criar-post', methods=["GET", "POST"])
def CriarPost():
    titulo = request.form.get('titulo')
    texto = request.form.get('texto')
    post = Post(titulo=titulo, texto=texto)
    db.session.add(post)
    db.session.commit()
    return redirect('/')

@app.route('/editar')
def editar():
    return redirect('/')

@app.route('/apagar', methods=["POST"])
def apagar():
    post_id = request.form.get("post_id")
    post = db.session.query(Post).filter(Post.id==post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/')

@app.route('/login', methods=["GET", "POST"])
def login():
    return redirect('/')

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
