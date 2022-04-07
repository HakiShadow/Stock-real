from servicios_web import rest_api
import requests

class Sesiones():

    def registro(nombre, email, passw):
        body = {
            "name": nombre,
            "email": email,
            "contraseña": passw
        }
        respuesta = requests.post(f'{rest_api.API_URL}/registro', json = body)
        return respuesta.status_code == 200

        