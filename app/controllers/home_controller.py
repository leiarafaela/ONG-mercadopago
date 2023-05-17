import mercadopago
from app import app
from flask import render_template, request
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/mp/meios', methods=['GET'])
def meios():
    sdk = mercadopago.SDK("TEST-6749706992397515-032221-80c67714fe6c5cbc6c321d6122c6f65c-346350990")

    payment_methods_response = sdk.payment_methods().list_all()
    payment_methods = payment_methods_response["response"]
    
    print(payment_methods)
    
 
@app.route('/mp/pagamento', methods=['POST'])
def criapagamento(valor):
    
    valorPagamento = 0
    
    for chave, valor in request.form.items():
        if chave == "valor":
            valorPagamento = valor
    
    base_url = "https://api.mercadopago.com"
     
    payment_data = { 
        "items": [
            {
                "title": "Doação - ONG",
                "description": "Doação para a Ong",
                "picture_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fpt%2Ffree-png-ikizz&psig=AOvVaw1QRDh4pAgkqK1oJ0Ul_-Yq&ust=1684372696597000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCID11bSX-_4CFQAAAAAdAAAAABAE",
                "category_id": "donate",
                "quantity": 1,
                "currency_id": "R$",
                "unit_price": valorPagamento
            }
        ]
    }
      
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer TEST-6749706992397515-032221-80c67714fe6c5cbc6c321d6122c6f65c-346350990"
    }

    response = requests.post(f"{base_url}/checkout/preferences", json=payment_data, headers=headers)

    if response.status_code == 201:
        payment = response.json()
        payment_url = payment["init_point"]
         
        return payment_url

    else:
        
        print("Erro ao criar pagamento:", response.status_code)
 
    