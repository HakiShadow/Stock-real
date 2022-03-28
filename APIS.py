from flask import Flask, jsonify, request
from datos.Modelos.Medicamentos import MedicamentosBD
import requests

app = Flask(__name__)

@app.route('/listar', methods=['GET'])
def listar():
    return jsonify(MedicamentosBD.listarMed())

# ___________________________________________________________________________________________________________

@app.route('/añadirMed', methods=['POST'])
def añadirMed():
    datosMed = request.get_json()
    if 'nombre' not in datosMed:
        return "Se requiere el nombre del medicamento", 400
    elif 'tipo' not in datosMed:
        return "Se requiere el tipo de medicamento", 400
    elif 'cantidad' not in datosMed:
        return "Se requiere la cantidad de medicamento que se agregara al stock", 400
    elif 'fecha' not in datosMed:
        return "Se requiere la fecha de vencimiento del medicamento", 400
    MedicamentosBD.agregarMed(datosMed['nombre'], datosMed['tipo'], datosMed['cantidad'], datosMed['fecha'], datosMed['descripcion'])
    return "OK", 200
# ___________________________________________________________________________________________________________
@app.route('/eliminar/<id>', methods = ['DELETE'])
def eliminar(id):
    MedicamentosBD.eliminarMed(id)
    return "OK", 200
# ___________________________________________________________________________________________________________
@app.route('/editarMed/<id>', methods = ['PUT'])
def editar(id):
    datosMed = request.get_json()
    if 'nombre' not in datosMed:
        return "Se requiere el nombre del medicamento", 400
    elif 'tipo' not in datosMed:
        return "Se requiere el tipo de medicamento", 400
    elif 'cantidad' not in datosMed:
        return "Se requiere la cantidad de medicamento que se agregara al stock", 400
    elif 'fecha' not in datosMed:
        return "Se requiere la fecha de vencimiento del medicamento", 400
    MedicamentosBD.editarMed(id, datosMed)
    return "OK", 200

@app.route('/select/<id>', methods=['GET'])
def select(id):
    return jsonify(MedicamentosBD.select(id))
# ___________________________________________________________________________________________________________
if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
  