from tkinter import *
from tkinter import messagebox as mb
import random

class Aplicacion:
    def __init__(self,ventana):
        self.label1=Label(ventana, text="Seleccione la cantidad de bultos:")
        self.label1.grid(column=0, row=0, padx=10, pady=10)
        self.spinbox1=Spinbox(ventana, from_=0, to=100, width=10, state='readonly')            
        self.spinbox1.grid(column=1, row=0, padx=10, pady=10)
        self.spinbox1.bind("<Button>",self.sortear)
        self.boton1=Button(ventana, text="Sortear", command=self.sortear)
        self.boton1.grid(column=0, row=1, padx=10, pady=10)
        self.label2=Label(ventana, text="", width=20)
        self.label2.grid(column=1, row=1, padx=10, pady=10)
        

    def sortear(self,*args):
        if int(self.spinbox1.get())==0:
            mb.showerror("Cuidado","Debe seleccionar un valor distinto a cero en bultos")
        else:
            valor=random.randint(1,3)
            if valor==1:
                self.label2.configure(text="Se deben revisar")
                self.label2.configure(background="red")
            else:
                self.label2.configure(text="No se revisan")
                self.label2.configure(background="green")
    
class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("SpinBox")
        w = 400
        h = 200
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w,h,x,y))
        self.resizable(False,False)
app=App()
Aplicacion(app)
app.mainloop()