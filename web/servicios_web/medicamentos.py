import requests
from datetime import datetime
from servicios_web import rest_api

class webServiciosMed():
    def ListarMed():
        respuesta = requests.get(f'{rest_api.API_URL}/listar')
        return respuesta.json()

    def select(id):
        respuesta = requests.get(f'{rest_api.API_URL}/select/{id}')
        return respuesta.json()

    def EliminarMed(id):
        respuesta = requests.delete(f'{rest_api.API_URL}/eliminar/{id}')
        return respuesta.status_code == 200

    def añadirMed(nombre, tipo, cantidad, fecha, descripcion):
        date= datetime.strptime(fecha, "%Y-%m")
        nuevaFecha=date.strftime("%Y/%m")

        body = {
            "nombre": nombre,
            "tipo": tipo,
            "cantidad": cantidad,
            "fecha": nuevaFecha,
            "descripcion": descripcion
        }
        respuesta = requests.post(f'{rest_api.API_URL}/añadirMed', json = body)
        return respuesta.status_code == 200

    def editarMed(id, nombre, tipo, cantidad, fecha, descripcion):
        date= datetime.strptime(fecha, "%Y-%m")
        nuevaFecha=date.strftime("%Y/%m")

        body = {
            "id": id,
            "nombre": nombre,
            "tipo": tipo,
            "cantidad": cantidad,
            "fecha": nuevaFecha,
            "descripcion": descripcion
        }
        respuesta = requests.put(f'{rest_api.API_URL}/editarMed/{id}', json = body)
        return respuesta.status_code == 200

