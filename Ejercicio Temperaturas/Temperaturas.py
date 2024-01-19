import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
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
        self.ventana.mainloop()



app=Temperaturas()