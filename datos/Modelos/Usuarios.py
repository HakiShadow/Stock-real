from datos.Tablas.Crear_base_de_datos import DataBase

bd = DataBase()

class sesiones():

    def registro(name, email, contraseña):
        sentencia_sql = f"""
            INSERT INTO Usuarios (nombre, mail, pass)
            VALUES ('{name}', '{email}', '{contraseña}')
        """
        bd.EjecutarSQL(sentencia_sql)