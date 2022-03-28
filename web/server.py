
from flask import Flask, request, redirect, url_for, session, render_template
from servicios_web.medicamentos import webServiciosMed

app = Flask(__name__, template_folder='templates')

# ___________________________________________________________________________________________________________

@app.route('/')
def landing():
    meds = webServiciosMed.ListarMed() or []
    return render_template('medicamentos.html', meds=meds)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('inicioSesion.html')

@app.route('/registro', methods = ['GET', 'POST'])
def registro():
    return render_template('registro.html')

@app.route('/cerrarsesion')
def cerrarSesion():
    #termina la sesion y redirije al login
    return render_template('inicioSesion.html')
# ___________________________________________________________________________________________________________

@app.route('/subirmed', methods = ['POST'])
def subirmed():
    nuevoMed = request.form
    if 'descripcion' not in nuevoMed:
        nuevoMed['descripcion'] = ""
    webServiciosMed.añadirMed(nuevoMed['nombre'], nuevoMed['tipo'], 
                        nuevoMed['cantidad'], nuevoMed['fecha'], 
                        nuevoMed['descripcion'])
    return redirect('/')

# ___________________________________________________________________________________________________________
    
@app.route('/trash/<id>')
def eliminar(id):
    webServiciosMed.EliminarMed(id)
    return redirect('/')
# ___________________________________________________________________________________________________________

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def editar(id):
    print(f'{id}')
    if request.method == 'POST':
        datosMed = request.form
        if 'descripcion' not in datosMed:
           datosMed['descripcion'] = ""
        webServiciosMed.editarMed(id, datosMed['nombre'], datosMed['tipo'], 
                        datosMed['cantidad'], datosMed['fecha'], 
                        datosMed['descripcion'])
        return redirect('/')
    meds = webServiciosMed.select(id) or []
    return render_template('editarMed.html', meds=meds)


# ___________________________________________________________________________________________________________

if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)