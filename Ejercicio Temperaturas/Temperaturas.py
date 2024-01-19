import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import PhotoImage
import CalculoTemperatura

class Temperaturas:

    def __init__(self):
        self.ctemperatura=CalculoTemperatura.Calculos
        self.ventana=tk.Tk()
        self.ventana.title("Calcular Temperatura")
        self.ventana.resizable(False,False)
        self.ventana.configure(background="#70A3CC")
        w = 525
        h = 400
        x = (self.ventana.winfo_screenwidth() /2) - (w /2)
        y = (self.ventana.winfo_screenheight() /2) - (w /2)
        self.ventana.geometry('%dx%d+%d+%d' % (w,h,x,y))
        self.Ingresar()
        self.ventana.mainloop()


    def Ingresar(self):
        #solecito = PhotoImage(file="Ejercicios Temperaturas/sol.png")
        #self.sol_label=ttk.Label(image=solecito)
        #self.sol_label.grid(column=0,row=0)
        #==============================CELSIUS======================================
        self.celsius_label =ttk.Label(self.ventana,text="Celsius",background="#70A3CC",font="20")
        self.celsius_label.grid(column=0,row=0,padx=4,pady=4)

        self.celsius_valor=tk.DoubleVar()
        self.celsius_entry= ttk.Entry(self.ventana,textvariable=self.celsius_valor,width=15)
        self.celsius_entry.grid(column=1,row=0,padx=4,pady=4)
        

        self.botonmas=ttk.Button(self.ventana,text="+1",width=4,command=self.sumar_c)
        self.botonmas.grid(column=2,row=0,padx=4,pady=4)
        self.botonmenos=ttk.Button(self.ventana,text="-1",width=4,command=self.restar_c)
        self.botonmenos.grid(column=3,row=0,padx=4,pady=4)

        #==============================FARENHEIT====================================
        self.farenheit_label =ttk.Label(self.ventana,text="Farenheit",background="#70A3CC",font="20")
        self.farenheit_label.grid(column=0,row=1,padx=4)
        self.farenheit_valor=tk.DoubleVar()
        self.farenheit_entry= ttk.Entry(self.ventana,textvariable=self.farenheit_valor,width=15)
        self.farenheit_entry.grid(column=1,row=1,padx=4,pady=4)


        self.botonmas=ttk.Button(self.ventana,text="+1",width=4,command=self.sumar_f)
        self.botonmas.grid(column=2,row=1,padx=4,pady=4)
        self.botonmenos=ttk.Button(self.ventana,text="-1",width=4,command=self.restar_f)
        self.botonmenos.grid(column=3,row=1,padx=4,pady=4)
        
        #==============================KELVIN======================================
        self.kelvin_label =ttk.Label(self.ventana,text="Kelvin",background="#70A3CC",font="20")
        self.kelvin_label.grid(column=0,row=2,padx=4)
        self.kelvin_valor=tk.DoubleVar()
        self.kelvin_entry= ttk.Entry(self.ventana,textvariable=self.kelvin_valor,width=15)
        self.kelvin_entry.grid(column=1,row=2,padx=4,pady=4)
        

        self.botonmas=ttk.Button(self.ventana,text="+1",width=4,command=self.sumar_k)
        self.botonmas.grid(column=2,row=2,padx=4,pady=4)
        self.botonmenos=ttk.Button(self.ventana,text="-1",width=4,command=self.restar_k)
        self.botonmenos.grid(column=3,row=2,padx=4,pady=4)

        #celsius_entry.trace("w",funcion)
        self.celsius_valor.trace_add("write",self.actualizar_C())
        self.farenheit_valor.trace_add("write",self.actualizar_F())
        self.kelvin_valor.trace_add("write",self.actualizar_K())
#==================================SUMAR-RESTAR===================================
    def sumar_c(self): self.celsius_valor.set(self.celsius_valor.get()+1)
    def sumar_f(self): self.farenheit_valor.set(self.farenheit_valor.get()+1)
    def sumar_k(self): self.kelvin_valor.set(self.kelvin_valor.get()+1)
    def restar_c(self): self.celsius_valor.set(self.celsius_valor.get()-1)
    def restar_f(self): self.farenheit_valor.set(self.farenheit_valor.get()-1)
    def restar_k(self): self.kelvin_valor.set(self.kelvin_valor.get()-1)

    def actualizar_C(self):
        #mb.showinfo("Alerta",self.celsius_entry.get())
        self.farenheit_valor.set(((self.celsius_valor.get()*9)/5)+32)
        self.kelvin_valor.set(self.celsius_valor.get() + 273.15)

    def actualizar_F(self):
        self.celsius_valor.set(((self.farenheit_valor.get()-32)*5) /9)
        self.kelvin_valor.set(((self.farenheit_valor.get()-32)*5)/9 + 273.15)

    def actualizar_K(self):
        self.celsius_valor.set(self.kelvin_valor.get() -273.15)
        self.farenheit_valor.set(((self.kelvin_valor.get()-273.15)*9)/5 + 32)

app=Temperaturas()