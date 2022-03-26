from datos.Tablas.Crear_base_de_datos import DataBase

bd = DataBase()

def agregarMed(nombre, tipo, cantidad, fecha, descripcion):
    sentencia_sql = f"""
    INSERT INTO Medicamentos (nombre, tipo, cantidad, fecha, descripcion)
    VALUES ('{nombre}', '{tipo}', '{cantidad}', STR_TO_DATE('{fecha}',"%Y/%m"), '{descripcion}')
    """
    bd.EjecutarSQL(sentencia_sql)

def editarMed(id, datosMed):
    sentencia_sql = f"""
    UPDATE Medicamentos
    SET
    nombre = '{datosMed["nombre"]}',
    tipo = '{datosMed["tipo"]}',
    cantidad = '{datosMed["cantidad"]}',
    fecha = STR_TO_DATE('{datosMed["fecha"]}',"%Y/%m"),
    descripcion = '{datosMed["descripcion"]}'
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
    print(f'{id}')
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





