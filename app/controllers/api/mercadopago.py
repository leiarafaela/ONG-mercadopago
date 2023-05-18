import mercadopago
import json

CLIENT_ID = '6749706992397515'
CLIENT_SECRET = 'wTHIj88ASrUCI0qpZ7apIUjbx9Fnjod1'


def payment(valorPagamento):
    valor =  int(valorPagamento)
    preference = { 
        "items": [
            {
                "title": "Doação - ONG",
                "description": "Doação para a Ong",
                "picture_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fpt%2Ffree-png-ikizz&psig=AOvVaw1QRDh4pAgkqK1oJ0Ul_-Yq&ust=1684372696597000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCID11bSX-_4CFQAAAAAdAAAAABAE",
                "category_id": "donate",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": valor
            }
        ]
    }

    mp = mercadopago.SDK("TEST-6749706992397515-032221-80c67714fe6c5cbc6c321d6122c6f65c-346350990")

    preferenceResult = mp.preference().create(preference)

    url = preferenceResult["response"]["init_point"]
    
    return url