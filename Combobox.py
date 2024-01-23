import tkinter as tk 
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.label1=ttk.Label(text="Ingrese Nombre: ").grid(column=0,row=0)
        self.nombre=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana,width=40,textvariable=self.nombre)
        self.entry1.grid(column=0,row=1)

        self.label2=ttk.Label(text="Seleccione pais").grid(column=0,row=2)
        self.pais=tk.StringVar()
        paises=("Argentina","Chile","Bolivia","Paraguay","Brasil","Uruguay")
        self.combobox1=ttk.Combobox(self.ventana,width=10,textvariable=self.pais,values=paises,state='readonly')
        try:
            n= paises.index("Brasil")
        except Exception as e:
            n =0
        self.combobox1.current(n)
        self.combobox1.grid(column=0,row=3)
        self.boton1=ttk.Button(self.ventana,text="Recuperar",command=self.mostrardatos)
        self.boton1.grid(column=0,row=4)
        self.ventana.mainloop()
    
    def mostrardatos(self):
        self.ventana.title("Nombre: " + self.nombre.get()+ " Pais: " + self.combobox1.get())

app = Aplicacion()