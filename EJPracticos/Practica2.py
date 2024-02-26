import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.base()
        self.contenido()
        self.grupo=[]
    def contenido(self):
        filas=(3,4,5,6)
        self.vFilas=tk.IntVar()
        self.tFilas=ttk.Combobox(self,values=filas,textvariable=self.vFilas,state="readonly",width=10)
        self.tFilas.grid(column=0,row=0)
        self.tFilas.bind("<<ComboboxSelected>>",self.rellenar)
    
    def rellenar(self,*args):
        item = self.vFilas.get()
        
        for o in self.grupo:
            o.destroy()
            
        contador = 1
        self.grupo=[]
        for i in range(0,item) :
            for u in range(1,item+1):
                label= tk.Label(self,text=contador)
                label.grid(column=i,row=u)
                self.grupo.append(label)
                contador=contador+1
    def base(self):
        self.title("CAJERO")
        w = 900
        h = 500
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)
        
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False, False)
        self.configure(background="#5A5352")        
        
app = App()
app.mainloop()