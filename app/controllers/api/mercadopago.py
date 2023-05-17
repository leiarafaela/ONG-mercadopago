import mercadopago
import os

sdk = mercadopago.SDK("TEST-6749706992397515-032221-80c67714fe6c5cbc6c321d6122c6f65c-346350990")

# Cria um item na preferência
preference_data = {
    "items": [
        {
            "title": "Doação",
            "quantity": 1,
            "unit_price": 105.50
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]




#client_id = os.

# mp = mercadopago.MP("TEST-a76ed238-da3e-4281-9e99-9c4eb2ef57c8", "TEST-6749706992397515-032221-80c67714fe6c5cbc6c321d6122c6f65c-346350990")


# payment_data = {
#     "transaction_amount": 100.0,
#     "description": "Compra de exemplo",
#     "payment_method_id": "visa",
#     "payer": {
#         "email": "comprador@teste.com"
#     }
# }
 
# payment = mp.post("/v1/payments", payment_data)
 
# if payment["status"] == 201:
#     payment_url = payment["response"]["init_point"]
#     print("URL do pagamento:", payment_url)
# else:
#     print("Erro ao criar pagamento:", payment["status"])
