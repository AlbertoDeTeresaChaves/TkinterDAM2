import tkinter as tk
from tkinter import ttk

class Contenido:
    def __init__(self,ventana):
        ttk.Label(ventana,text="Primer numero: ").grid(column=0,row=0,padx=5,pady=5)
        self.numero1=tk.IntVar()
        self.numero1entry=ttk.Entry(ventana,width=10,textvariable=self.numero1)
        self.numero1entry.grid(column=1,row=0)
        self.numero1entry.bind("<Return>",self.calculo)
        self.numero1entry.bind("<FocusOut>",self.calculo)

        self.label2=ttk.Label(ventana,text="Operacion: ").grid(column=0,row=1,padx=5,pady=5)
        self.operador=tk.StringVar()
        operaciones=("+","-","*","/")
        self.combobox1=ttk.Combobox(ventana,width=10,textvariable=self.operador,values=operaciones,state='readonly')
        self.combobox1.grid(column=1,row=1)
        try:
            n = operaciones.index("+")
        except Exception as e:
            n = 0
        self.combobox1.current(n)
        self.combobox1.bind("<<ComboboxSelected>>",self.calculo)

        ttk.Label(ventana,text="Segundo numero: ").grid(column=0,row=2,padx=5,pady=5)
        self.numero2=tk.IntVar()
        self.numero2entry=ttk.Entry(ventana,width=10,textvariable=self.numero2)
        self.numero2entry.grid(column=1,row=2)
        self.numero2entry.bind("<Return>",self.calculo)
        self.numero2entry.bind("<FocusOut>",self.calculo)

        self.boton1=tk.Button(ventana,text="Calcular",command=self.calculo )
        self.boton1.grid(column=0,row=3)
        self.label1=ttk.Label(ventana)
        self.label1.grid(column=1,row=3)

        app.mainloop()

    def calculo(self,*args):
        n=eval(str(self.numero1.get())+self.combobox1.get()+str(self.numero2.get()))
        self.label1.config(text=str(n))
  
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        w = 400
        h = 200
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w,h,x,y))
        self.resizable(False,False)

app=App()
Contenido(app)
