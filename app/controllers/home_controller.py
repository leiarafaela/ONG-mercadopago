from flask import render_template, request, redirect
import mercadopago

from app import app
from ..api.mercadopago import payment



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
    return redirect(payment(valorPagamento))
