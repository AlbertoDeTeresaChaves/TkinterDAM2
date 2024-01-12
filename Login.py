import tkinter as tk
from tkinter import ttk

class Application:
    def __init__(self):
        self.ventana=tk.Tk()
        
        self.usuario=ttk.Label(text="Ingrese su usuario:")
        self.usuario.grid(column=0,row=0)

        #Recoge el usuario
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana,width=30,textvariable=self.dato1)
        self.entry1.grid(column=1,row=0)

        self.contraseña=ttk.Label(text="Ingrese contraseña:")
        self.contraseña.grid(column=0,row=1)

        #Recoge la contraseña
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana,width=30,textvariable=self.dato2,show="*")
        self.entry2.grid(column=1,row=1)

        self.boton1=ttk.Button(self.ventana,text="ENTER",command=self.ingresar)
        self.boton1.grid(column=1,row=2)
        self.ventana.mainloop()

    def ingresar(self):
        if self.dato1.get()=="juan" and self.dato2.get()=="abc123":
            self.ventana.title("Correcto")
        else:
            self.ventana.title("Incorrecto")

#MAIN

Aplicacion=Application()
