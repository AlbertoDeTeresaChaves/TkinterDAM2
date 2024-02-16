import mysql.connector

class Banco:
    
    def obtener():
        conexion = mysql.connector.connect(host="localhost",user="root",passwd="root",database="bankia")
        cursor=conexion.cursor()
        SQL_SELECT="SELECT * FROM CAJERO ORDER BY MONEDA DESC"
        cursor.execute(SQL_SELECT)
        vuelta=cursor.fetchall()
        return vuelta
