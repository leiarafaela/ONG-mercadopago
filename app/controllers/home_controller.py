from app import app
from flask import render_template
from models.doador import Doador

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/home', methods=['POST'])
def criar_doador():
    infos_doador = {}
    create_doador = Doador.create(infos_doador)

    return create_doador
