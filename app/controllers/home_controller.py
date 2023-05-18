import mercadopago
import requests

from app import app
from ..models.doador import Doador
from .api.mercadopago import payment
from flask import render_template, request, redirect
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options


@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')

 
@app.route('/mp/meios', methods=['GET'])
def meios():
    sdk = mercadopago.SDK("TEST-6749706992397515-032221-80c67714fe6c5cbc6c321d6122c6f65c-346350990")

    payment_methods_response = sdk.payment_methods().list_all()
    payment_methods = payment_methods_response["response"]
    
    print(payment_methods)
    
 
@app.route('/mp/pagamento', methods=['POST'])
def criar_pagamento():
    infos_doador = {}
    for chave, valor in request.form.items():
        if chave == "valor":
            valorPagamento = valor
        
        infos_doador[chave] = valor
        
    create_doador = Doador.create(infos_doador)

    return redirect(payment(valorPagamento))


# Criação do doador já está sendo feita no função criar_pagamento
@app.route('/home', methods=['POST'])
def criar_doador():
    infos_doador = {}
    for chave, valor in request.form.items():
        infos_doador[chave] = valor

    create_doador = Doador.create(infos_doador)

    return create_doador
