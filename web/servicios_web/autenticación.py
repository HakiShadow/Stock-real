from servicios_web import rest_api
import requests

def registro(usuario, email, contraseña):
    body = {
        "usuario": usuario,
        "email": email,
        "contraseña": contraseña
    }
    respuesta = requests.post(f'{rest_api.API_URL}/registar', json = body)
    return respuesta.status_code == 200

def login(usuario, email, contraseña):
    pass

