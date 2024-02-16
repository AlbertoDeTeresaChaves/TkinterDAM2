from tkinter import *
import consultas



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
        w = 700
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
app = App()
app.mainloop()