from Crear_base_de_datos import DataBase

sql_tabla_medicamentos = '''
CREATE TABLE Medicamentos (
idmed  INTEGER PRIMARY KEY AUTO_INCREMENT,
nombre CHAR(30) NOT NULL UNIQUE,
tipo VARCHAR(50) NOT NULL,
cantidad INTEGER NOT NULL,
fecha DATE NOT NULL,
descripcion TEXT(256))
'''

sql_tabla_usuarios = '''
CREATE TABLE Usuarios (
idusuario INTEGER PRIMARY KEY AUTO_INCREMENT,
nombre CHAR(20) NOT NULL,
nombreUsuario VARCHAR(20) NOT NULL UNIQUE,
mail VARCHAR(40) NOT NULL,
pass VARCHAR(20) NOT NULL
)
'''

if __name__ == '__main__':
    try:
        print('Abriendo conexión con la base de datos...')
        conexion = DataBase.__init__(DataBase)

        print('Creando las tablas...')
        DataBase.CrearTablas(DataBase, sql_tabla_medicamentos)
        DataBase.CrearTablas(DataBase, sql_tabla_usuarios)     
        print('Creación finalizada.')

    except Exception as e:
        print (f'Un error a ocurrido {e}')