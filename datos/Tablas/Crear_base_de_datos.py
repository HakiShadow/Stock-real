import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect (
            host = 'localhost',
            user = 'root',
            password = 'lealeo321',
            db = 'farm'
        )
        self.cursor = self.connection.cursor()

    def CerrarConexion(self):
        self.connection.close()

    def EjecutarSQL(self, sql):
        self.__init__() #Iniciar la conexion

        cur = self.cursor
        cur.execute(sql)
        
        filas = cur.fetchall()

        self.connection.commit()
        self.CerrarConexion()

        return filas

    def CrearTablas(self, sql):
        self.__init__(self) #Iniciar la conexion
        
        cur = self.cursor
        cur.execute(sql)

        self.connection.commit()
        self.CerrarConexion(self)