from tkinter import *
from tkinter import messagebox as mb
import random

class Aplicacion():
    def __init__(self,ventana):
        self.label1 = Label(ventana,text="Color Rojo",width=10).grid(column=0, row=0, padx=10, pady=10)
        self.spinbox1 = Spinbox(ventana, from_=0, to=255, width=10, state='readonly')
        self.spinbox1.bind("<Button>",self.cambioColor)
        self.spinbox1.grid(column=1, row=0, padx=10, pady=10)

        self.color = Label(ventana,width=20)
        self.color.grid(column=2,row=0)

        self.label2 = Label(ventana,text="Color Verde",width=10).grid(column=0, row=1, padx=10, pady=10)
        self.spinbox2 = Spinbox(ventana, from_=0, to=255, width=10, state='readonly')
        self.spinbox2.bind("<Button>",self.cambioColor)
        self.spinbox2.grid(column=1, row=1, padx=10, pady=10)

        self.label3 = Label(ventana,text="Color Azul",width=10).grid(column=0, row=2, padx=10, pady=10)
        self.spinbox3 = Spinbox(ventana, from_=0, to=255, width=10, state='readonly')
        self.spinbox3.bind("<Button>",self.cambioColor)
        self.spinbox3.grid(column=1, row=2, padx=10, pady=10)
        self.cambioColor()
    
    def cambioColor(self,*args):
        mitupla=(int(self.spinbox1.get()),int(self.spinbox2.get()),int(self.spinbox3.get()))
        self.color.configure(background=rgb_color(mitupla))

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
def rgb_color(rgb):
    return '#%02x%02x%02x' % rgb
app=App()
Aplicacion(app)
app.mainloop()