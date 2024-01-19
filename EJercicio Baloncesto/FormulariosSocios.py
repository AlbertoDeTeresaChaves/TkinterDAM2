import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import Socio

class FormularioSocio:
    def __init__(self):
        self.socio=Socio.Socio()
        self.ventana=tk.Tk()
        self.ventana.title("Socios de Baloncesto")
        self.cuaderno=ttk.Notebook(self.ventana)
        self.Insertar()
        self.consultarSocio()
        self.listado_completo()
        self.borrado()
        self.modificar()

        self.cuaderno.grid(column=0,row=0,padx=10,pady=10)
        self.ventana.resizable(False,False)
        self.ventana.configure(background="gray")
        w = 525
        h = 400
        x = (self.ventana.winfo_screenwidth() /2) - (w /2)
        y = (self.ventana.winfo_screenheight() /2) - (w /2)
        self.ventana.geometry('%dx%d+%d+%d' % (w,h,x,y))
        self.ventana.mainloop()

    def Insertar(self):
        self.pagina1 =ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina1,text="Insertar Socio")

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
        datos=(self.socioID.get(), self.nombre.get(),self.estatura.get(),self.edad.get(),self.localidad.get())
        self.socio.nuevo_socio(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.socioID.set("")
        self.nombre.set("")
        self.estatura.set("")
        self.edad.set("")
        self.localidad.set("")

    def consultarSocio(self):
        self.pagina2=ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina2,text="Consultar Socio")

        self.labelframe2=ttk.LabelFrame(self.pagina2,text="Consulta:")
        self.labelframe2.grid(column=0,row=0,padx=5,pady=10)

        #==============================SOCIOID==================================
        self.label6=ttk.Label(self.labelframe2,text="socioID:")
        self.label6.grid(column=0,row=0,padx=4,pady=4)

        self.socioID2=tk.IntVar()
        self.entrySocioID2=ttk.Entry(self.labelframe2,textvariable=self.socioID2)
        self.entrySocioID2.grid(column=1,row=0,padx=4,pady=4)

        #==============================NOMBRE====================================
        self.label10=ttk.Label(self.labelframe2,text="Nombre:")
        self.label10.grid(column=0,row=1,padx=4,pady=4)

        self.nombre2=tk.StringVar()
        self.entrynombre2=ttk.Entry(self.labelframe2,textvariable=self.nombre2,state="readonly")
        self.entrynombre2.grid(column=1,row=1,padx=4,pady=4)
        #==============================ESTATURA===================================
        self.label7=ttk.Label(self.labelframe2,text="Estatura:")
        self.label7.grid(column=0,row=2,padx=4,pady=4)

        self.estatura2=tk.IntVar()
        self.entryestatura2=ttk.Entry(self.labelframe2,textvariable=self.estatura2,state="readonly")
        self.entryestatura2.grid(column=1,row=2,padx=4,pady=4)

        #=================================EDAD=====================================
        self.label8=ttk.Label(self.labelframe2,text="Edad:")
        self.label8.grid(column=0,row=3,padx=4,pady=4)

        self.edad2=tk.IntVar()
        self.entryedad2=ttk.Entry(self.labelframe2,textvariable=self.edad2,state="readonly")
        self.entryedad2.grid(column=1,row=3,padx=4,pady=4)

        #==============================LOCALIDAD====================================
        self.label9=ttk.Label(self.labelframe2,text="Localidad:")
        self.label9.grid(column=0,row=4,padx=4,pady=4)

        self.localidad2=tk.StringVar()
        self.entrylocalidad2=ttk.Entry(self.labelframe2,textvariable=self.localidad2,state="readonly")
        self.entrylocalidad2.grid(column=1,row=4,padx=4,pady=4)

        #=================================BOTON=====================================
        self.boton2=ttk.Button(self.labelframe2,text="Buscar",command=self.consultar)
        self.boton2.grid(column=1,row=5,padx=4,pady=4)

    def consultar(self):
        datos=(self.socioID2.get(),)
        respuesta = self.socio.consulta_socio(datos)
        if len(respuesta)>0:
            self.nombre2.set(respuesta[0][0])
            self.estatura2.set(respuesta[0][1])
            self.edad2.set(respuesta[0][2])
            self.localidad2.set(respuesta[0][3])
        else:
            self.socioID.set("")
            self.nombre.set("")
            self.estatura.set("")
            self.edad.set("")
            self.localidad.set("")
            mb.showerror("Error","No existe esa id")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina3, text="Listado completo")

        self.labelframe3=ttk.LabelFrame(self.pagina3,text="Socio")
        self.labelframe3.grid(column=0,row=0,padx=5,pady=10)

        self.boton1=ttk.Button(self.labelframe3,text="Listado completo",command=self.listar)
        self.boton1.grid(column=0,row=0,padx=4,pady=4)

        self.scrolledtext1=st.ScrolledText(self.labelframe3,width=30,height=10)
        self.scrolledtext1.grid(column=0,row=1,padx=10,pady=10)

    def listar(self):
        respuesta=self.socio.socios()
        self.scrolledtext1.delete("1.0",tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "socioID:"+str(fila[0])+
                                              "\nNombre:"+(fila[1])+
                                              "\nEstatura:"+str(fila[2])+
                                              "\nEdad:"+str(fila[3])+
                                              "\nLocalidad:"+(fila[4])+
                                              "\n\n")
    
    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina4,text="Borrado de Socio")

        self.labelframe4=ttk.LabelFrame(self.pagina4,text="Socio")
        self.labelframe4.grid(column=0,row=0,padx=5,pady=10)

        self.label11=ttk.Label(self.labelframe4,text="SocioID")
        self.label11.grid(column=0,row=0,padx=4,pady=4)

        self.codigoborra=tk.IntVar()
        self.entryborra=ttk.Entry(self.labelframe4,textvariable=self.codigoborra,text="")
        self.entryborra.grid(column=1,row=0,padx=10,pady=10)

        self.botonborrar=ttk.Button(self.labelframe4,text="Borrar",command=self.borrar)
        self.botonborrar.grid(column=1,row=1,padx=4,pady=4)

    def borrar(self):
        obtenerID=(self.entryborra.get(),)
        respuesta =self.socio.borrar_socio(obtenerID)
        if respuesta ==1:
            mb.showinfo("Borrado","Socio borrado")
            self.entryborra.set("")
        else:
            mb.showerror("Erro","No existe ningun Socio con esa ID")

    def modificar(self):
        self.pagina5=ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina5,text="Modificar Socio")

        self.labelframe5=ttk.LabelFrame(self.pagina5,text="Socio")
        self.labelframe5.grid(column=0,row=0,padx=5,pady=10)

        #==============================SOCIOID==================================
        self.label12=ttk.Label(self.labelframe5,text="socioID:")
        self.label12.grid(column=0,row=0,padx=4,pady=4)

        self.socioID3=tk.IntVar()
        self.entrySocioID3=ttk.Entry(self.labelframe5,textvariable=self.socioID3)
        self.entrySocioID3.grid(column=1,row=0,padx=4,pady=4)

        #==============================NOMBRE====================================
        self.label13=ttk.Label(self.labelframe5,text="Nombre:")
        self.label13.grid(column=0,row=1,padx=4,pady=4)

        self.nombre3=tk.StringVar()
        self.entrynombre3=ttk.Entry(self.labelframe5,textvariable=self.nombre3)
        self.entrynombre3.grid(column=1,row=1,padx=4,pady=4)
        #==============================ESTATURA===================================
        self.label14=ttk.Label(self.labelframe5,text="Estatura:")
        self.label14.grid(column=0,row=2,padx=4,pady=4)

        self.estatura3=tk.IntVar()
        self.entryestatura3=ttk.Entry(self.labelframe5,textvariable=self.estatura3)
        self.entryestatura3.grid(column=1,row=2,padx=4,pady=4)

        #=================================EDAD=====================================
        self.label15=ttk.Label(self.labelframe5,text="Edad:")
        self.label15.grid(column=0,row=3,padx=4,pady=4)

        self.edad3=tk.IntVar()
        self.entryedad3=ttk.Entry(self.labelframe5,textvariable=self.edad3)
        self.entryedad3.grid(column=1,row=3,padx=4,pady=4)

        #==============================LOCALIDAD====================================
        self.label16=ttk.Label(self.labelframe5,text="Localidad:")
        self.label16.grid(column=0,row=4,padx=4,pady=4)

        self.localidad3=tk.StringVar()
        self.entrylocalidad3=ttk.Entry(self.labelframe5,textvariable=self.localidad3)
        self.entrylocalidad3.grid(column=1,row=4,padx=4,pady=4)

        #=================================BOTON=====================================
        self.boton3=ttk.Button(self.labelframe5,text="Consular",command=self.consultar_mod)
        self.boton3.grid(column=1,row=5)

        self.boton4=ttk.Button(self.labelframe5,text="Modifica",command=self.modifica)
        self.boton4.grid(column=2,row=5)

    def consultar_mod(self):
        datos=(self.socioID3.get(),)
        respuesta = self.socio.consulta_socio(datos)
        if len(respuesta)>0:
            self.nombre3.set(respuesta[0][0])
            self.estatura3.set(respuesta[0][1])
            self.edad3.set(respuesta[0][2])
            self.localidad3.set(respuesta[0][3])
        else:
            self.socioID3.set("")
            self.nombre3.set("")
            self.estatura3.set("")
            self.edad3.set("")
            self.localidad3.set("")
            mb.showerror("Error","No existe esa id")
    
    def modifica(self):
        datos=(self.nombre3.get(),self.estatura3.get(),self.edad3.get(),self.localidad3.get(),self.socioID3.get())
        respuesta =self.socio.modificar(datos)
        if respuesta ==1:
            mb.showinfo("Aviso","Socio Actualizado")
        else:
            mb.showerror("Error","Imposible actualizarlo")
            
app=FormularioSocio()

