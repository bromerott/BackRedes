import pandas as pd
import mysql.connector
class controlador:
    dfUsuarios = pd.DataFrame(columns={'Nombre','Apellido'})
    
    def __init__(self):
        self.cargarUsuarios()

    def cargarUsuarios(self):
        #Cargar las puertas (nPuerta,Tipo,FlujoPersonas, Estado) desde la BD
        mydb = mysql.connector.connect(
            host="bdtaredes.c4wrsskhrcvn.us-east-1.rds.amazonaws.com",
            user="mainUserRedes",
            passwd="passRedes123456",
            port="3306",
            database="bdTARedes"
        )
        mydb.connect()
        self.dfUsuarios = pd.read_sql_query("SELECT nombre,apellido FROM Usuarios; ",mydb)
        self.dfUsuarios = self.dfUsuarios.rename(columns={"nombre":"Nombre","apellido":"Apellido"})
        mydb.close()  

    def listarUsuarios(self):
        self.cargarUsuarios()
        return self.dfUsuarios.to_json(orient='records')

    def insertarUsuario(self,nombre,apellido):
        mydb = mysql.connector.connect(
            host="bdtaredes.c4wrsskhrcvn.us-east-1.rds.amazonaws.com",
            user="mainUserRedes",
            passwd="passRedes123456",
            port="3306",
            database="bdTARedes"
        )
        mydb.connect()
        query = """ INSERT INTO `Usuarios`
                          (`nombre`, `apellido`) VALUES (%s,%s)"""
        insert_tuple = (nombre, apellido)            
        cursor = mydb.cursor(prepared=True)
        result  = cursor.execute(query,insert_tuple)
        mydb.commit()
        mydb.close()
        self.cargarUsuarios()