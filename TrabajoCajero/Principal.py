from tkinter import *
from tkinter import scrolledtext as st
import consultas
import mysql.connector


class CrearFrame(Frame):
    def __init__(self,ventana,ancho,color,posicion):
        super().__init__(bg=color,height=730,width=ancho,pady=40)
        self.contenido=ventana
        ipadding={"ipadx":10,"ipady":10}
        self.pack(**ipadding,side="left",padx=posicion)
        self.pack_propagate()

        
class Cspinbox(Spinbox):
  def __init__(self,ventana,fila,columna,variable):
      super().__init__()
      cadena2=("w"+str(variable)).replace(".","")
      nuevo=Spinbox(ventana,from_=0,to=globals()[cadena2].get(),justify="right",increment=1,textvariable=globals()[cadena2],width=5)        
      nuevo.grid(column=columna,row=fila)

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("CAJERO")
        w = 500
        h = 500
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)
        
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False, False)
        self.configure(background="#5A5352")
        self.marco1 = CrearFrame(self,180,"#5A5352",(10,40))
        self.marco2 = CrearFrame(self,420,"#5A5352",(10,40))
        self.rellenar()

    def rellenar(self):    
        textobold = {"foreground": "white", "background": "#5A5352", "font": "helvetica 11 bold",}
    #--------------------------------------------MARCO 1-------------------------------------------
        Label(self.marco1, text="MONEDA", **textobold).grid(column=0, row=0, padx=10)
        Label(self.marco1, text="CANTIDAD", **textobold).grid(column=1, row=0, padx=10, pady=5)
        fila=1

        for i in consultas.Banco.obtener():
            cadena = ("w"+str(i[0])).replace(".","")
            globals()[cadena]=DoubleVar(value=i[1])   
            Label(self.marco1,text=i[0],**textobold,width=5,anchor="w").grid(column=0,row=fila)       
            Cspinbox(self.marco1,fila,1,i[0])
            fila=fila+1
    #--------------------------------------------MARCO 2-------------------------------------------
        Label(self.marco2,text="COMPRA",**textobold).grid(column=0,row=0)
        self.compra=DoubleVar()
        self.compra=Spinbox(self.marco2,name="compra",from_=0,to=10000,increment=1,justify="right",textvariable=self.compra)
        self.compra.grid(column=0,row=1)
        Label(self.marco2,text="PAGO",**textobold).grid(column=0,row=2)
        self.scrolltext1= st.ScrolledText(self.marco2,width=20,height=10)
        self.scrolltext1.grid(column=0,row=3)
        Label(self.marco2,text="VUELTA",**textobold).grid(column=0,row=4)
        self.scrolltext2= st.ScrolledText(self.marco2,width=20,height=10)
        self.scrolltext2.grid(column=0,row=5)        

        boton =Button(self.marco2,text="REALIZAR COMPRA",command=self.operacion)
        boton.grid(column=0,row=6,padx=5,pady=5)

    def operacion(self):
        self.totaldinero = self.scrolltext1.get("1.0","end-1c")
        self.vuelta = self.scrolltext2
        tb = self.totaldinero.split('#')
        cantidad_total = 0.0
        for i in tb:
            matriz2 = i.split('-')
            cantidad_total += int(matriz2[0]) * float(matriz2[1])
        resto_cantidad = cantidad_total - float(self.compra.get())
        resto_cantidad = round(resto_cantidad, 2)
        self.scrolltext2=""
        if float(self.compra.get()) <= cantidad_total:
         try:
            sentencia = f"SELECT * from cajero where CANTIDAD > 0 order by MONEDA DESC"
            connection = mysql.connector.connect(host='localhost', database='bankia', user='root', password='root')
            cursor = connection.cursor()
            for i in tb:
                matriz2 = i.split('-')
                sentencia2 = f"UPDATE cajero set CANTIDAD = CANTIDAD + {matriz2[0]} where MONEDA = {matriz2[1]}"
                cursor.execute(sentencia2)
                connection.commit()
            while resto_cantidad > 0.01:
                cursor.execute(sentencia)
                records = cursor.fetchall()
                for row in records:
                    bbdd_cantidad = int(row[1])
                    bbdd_moneda = float(row[0])
                    if bbdd_moneda <= resto_cantidad:
                        resto = int(resto_cantidad / bbdd_moneda)

                        if resto <= bbdd_cantidad:
                            resto_cantidad = round(resto_cantidad - (bbdd_moneda * resto), 2)
                            sentencia3 = f"UPDATE cajero set CANTIDAD = CANTIDAD - {resto} where MONEDA = {bbdd_moneda}"
                            cursor.execute(sentencia3)
                            connection.commit()
                            self.scrolltext2 += f"{resto} {bbdd_moneda}\n"
                        else:
                            resto_cantidad = round(resto_cantidad - (bbdd_moneda * bbdd_cantidad), 2)
                            sentencia3 = f"UPDATE cajero set CANTIDAD = CANTIDAD - {bbdd_cantidad} where MONEDA = {bbdd_moneda}"
                            cursor.execute(sentencia3)
                            connection.commit()
                            self.scrolltext2 += f"{bbdd_cantidad} {bbdd_moneda}\n"
                self.vuelta.delete(1.0, END)
                self.vuelta.insert(INSERT, self.scrolltext2)
                
         except mysql.connector.Error as e:
            print(e)

         finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
        else:
         print(f"Debe ingresar {resto_cantidad} para completar la compra")
app = App()
app.mainloop()