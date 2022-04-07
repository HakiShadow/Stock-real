from src.datos.Tablas.Crear_base_de_datos import DataBase

bd = DataBase()

class MedicamentosBD():

    def agregarMed(nombre, tipo, cantidad, fecha, descripcion):

        sentencia_sql = f"""
        INSERT INTO Medicamentos (nombre, tipo, cantidad, fecha, descripcion)
        VALUES ('{nombre.capitalize()}', '{tipo.capitalize()}', '{cantidad}', STR_TO_DATE('{fecha}',"%Y/%m"), '{descripcion.capitalize()}')
        """
        bd.EjecutarSQL(sentencia_sql)

    def editarMed(id, datosMed):
        sentencia_sql = f"""
        UPDATE Medicamentos
        SET
        nombre = '{datosMed["nombre"].capitalize()}',
        tipo = '{datosMed["tipo"].capitalize()}',
        cantidad = '{datosMed["cantidad"]}',
        fecha = STR_TO_DATE('{datosMed["fecha"]}',"%Y/%m"),
        descripcion = '{datosMed["descripcion"].capitalize()}'
        WHERE
        idmed={id}
        """
        bd.EjecutarSQL(sentencia_sql)
        

    def listarMed():
        sentencia_sql = f"""
        SELECT * FROM Medicamentos ORDER BY fecha asc
        """
        return [{"id": med[0],
                "nombre": med[1],
                "tipo": med[2],    
                "cantidad": med[3],
                "fecha": med[4],
                "descripcion": med[5]} for med in bd.EjecutarSQL(sentencia_sql)]

    def select(id):
        sentencia_sql = f"""
        SELECT * FROM Medicamentos WHERE idmed={id}
        """
        return [{"id": med[0],
                "nombre": med[1],
                "tipo": med[2],    
                "cantidad": med[3],
                "fecha": med[4],
                "descripcion": med[5]} for med in bd.EjecutarSQL(sentencia_sql)]

    def eliminarMed(id):
        sentencia_sql = f"""
        DELETE FROM Medicamentos WHERE idmed={id}
        """
        bd.EjecutarSQL(sentencia_sql)








