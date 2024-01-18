import tkinter as tk
from tkinter import ttk
import Socio

class FormularioSocio:
    def __init__(self):
        self.socio=Socio.Socio()
        self.ventana=tk.Tk()
        self.ventana.title("Socios de Baloncesto")
        self.cuaderno=ttk.Notebook(self.ventana)
        self.Insertar()

        self.cuaderno.grid(column=0,row=0,padx=10,pady=10)
        self.ventana.mainloop()

    def Insertar(self):
        self.pagina1 =ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.cuaderno,text="Insertar Socio")

        self.labelframe1=ttk.LabelFrame(self.pagina1,text="Socio")
        self.labelframe1.grid(column=0,row=0,padx=5,pady=10)

        #==============================SOCIOID==================================
        self.label1=ttk.Label(self.labelframe1,text="socioID:")
        self.label1.grid(column=0,row=0,padx=4,pady=4)

        self.socioID=tk.IntVar()
        self.entrySocioID=ttk.Entry(self.labelframe1,textvariable=self.socioID)
        self.entrySocioID.grid(column=1,row=0,padx=4,pady=4)

        #==============================NOMBRE====================================
        self.label2=ttk.Label(self.labelframe1,text="Nombre:")
        self.label2.grid(column=0,row=1,padx=4,pady=4)

        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1,textvariable=self.nombre)
        self.entrynombre.grid(column=1,row=1,padx=4,pady=4)

        #==============================ESTATURA===================================
        self.label3=ttk.Label(self.labelframe1,text="Estatura:")
        self.label3.grid(column=0,row=2,padx=4,pady=4)

        self.estatura=tk.IntVar()
        self.entryestatura=ttk.Entry(self.labelframe1,textvariable=self.estatura)
        self.entryestatura.grid(column=1,row=2,padx=4,pady=4)

        #=================================EDAD=====================================
        self.label4=ttk.Label(self.labelframe1,text="Edad:")
        self.label4.grid(column=0,row=3,padx=4,pady=4)

        self.edad=tk.IntVar()
        self.entryedad=ttk.Entry(self.labelframe1,textvariable=self.edad)
        self.entryedad.grid(column=1,row=3,padx=4,pady=4)

        #==============================LOCALIDAD====================================
        self.label5=ttk.Label(self.labelframe1,text="Localidad:")
        self.label5.grid(column=0,row=4,padx=4,pady=4)

        self.localidad=tk.StringVar()
        self.entrylocalidad=ttk.Entry(self.labelframe1,textvariable=self.localidad)
        self.entrylocalidad.grid(column=1,row=4,padx=4,pady=4)

        #=================================BOTON=====================================
        self.boton1=ttk.Button(self.labelframe1,text="Confirmar",command=self.BInsertar)
        self.boton1.grid(column=1,row=5,padx=4,pady=4)
        
    def BInsertar(self):
        datos=(self.socioID.get(),self.nombre.get(),self.estatura.get())


