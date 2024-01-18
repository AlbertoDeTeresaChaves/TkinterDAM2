import mysql.connector

class Socio:
    def __init__(self):
        self.conexion=mysql.connector.connect(host="localhost",user="root",passwd="root",database="baloncesto")

    def nuevo_socio(self,datos):
        cursor=self.conexion.cursor()
        sql="insert into socio(socioID,nombre,estatura,edad,localidad) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql,datos)
        self.conexion.commit()

    def consulta_socio(self,datos):
        cursor=self.conexion.cursor()
        sql="select nombre,estatura,edad,localidad from socio where socioID=%s"
        cursor.execute(sql,datos)
        vuelta=cursor.fetchall()
        return vuelta
    
    def socios(self):
        cursor=self.conexion.cursor()
        sql="select socioID,nombre,estatura,edad,localidad from socio"
        cursor.execute(sql)
        vuelta=cursor.fetchall()
        return vuelta
    
    def borrar_socio(self,datos):
        cursor=self.conexion.cursor()
        sql="delete from socio where socioID=%s"
        cursor.execute(sql,datos)
        n=cursor.rowcount
        self.conexion.commit()
        return n # retornamos la cantidad de filas borradas
    
    def modificar(self,datos):
        cursor=self.conexion.cursor()
        sql="update socio set nombre=%s,estatura=%s,edad=%s,localidad=%s where socioID=%s"
        cursor.execute(sql,datos)
        n=cursor.rowcount
        self.conexion.commit()
        return n # retornamos la cantidad de filas modificadas
