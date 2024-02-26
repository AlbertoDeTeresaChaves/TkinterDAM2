

class Consulta:
    def __init__(self):
        self.conexion=mysql.connector.connect(host="localhost",user="root",passwd="root",database="baloncesto")
#SELECT ENAME,EMPNO FROM EMP WHERE EMPNO IN(SELECT DISTINCT MGR FROM EMP WHERE MGR IS NOT NULL) ORDER BY 1
    def nuevoEmpleado(self,datos):
        cursor=self.conexion.cursor()
        SQL_INSERT="INSERT INTO emp values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(SQL_INSERT)
        self.conexion.commit()
class base:
    def verificar():
        try:
            connection = mysql.connector.connect(host='localhost', database='sys', user='root', password='root')
            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute("CREATE DATABASE CAJEROS")
                print("Base de datos creada")

        except mysql.connector.Error as e:
            print("BBDD conectada")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def verificartbl():
        SQL_CREATE = "CREATE TABLE CAJERO(MONEDA DECIMAL(10,2) PRIMARY KEY, CANTIDAD INT CHECK(CANTIDAD>=0))"
        SQL_INSERT = "INSERT INTO CAJERO VALUES (%s, %s)"
        numeros = [5, 2, 1]

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="CAJEROS")
            cursor = conn.cursor()

            cursor.execute(SQL_CREATE)
            print("Tabla creada")
            for i in range(-2, 3):
                for j in range(len(numeros)):
                    cursor.execute(SQL_INSERT, (10 ** i * numeros[j], 10))

            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print("Tabla conectada")