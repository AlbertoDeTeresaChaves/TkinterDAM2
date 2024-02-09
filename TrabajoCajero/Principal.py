from tkinter import *



class Inicio(Frame):
    def __init__(self,ventana):
        self.titulo=Label(ventana,text="CAJERO",background="#5A5352",font=30,justify="center").grid(column=0,columnspan=10)

        self.verCajero=Label(ventana,text="Ver Cajero",foreground="white",background="#5A5352").grid(column=0,row=1)
        self.bMostrarCajero=Button(ventana,text="VER",background="RED",command=self.cambio(Inicio2))
        self.bMostrarCajero.grid(column=0,row=2,padx=15)


    def cambio(self,opcion):
        new_frame=opcion(self)
        self._frame = new_frame
        self._frame.pack()

class Inicio2(Frame):
    def __init__(self,ventana):
        self.titulo=Label(ventana,text="HOLA").grid(column=0,row=0)


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("CAJERO")
        w = 600
        h = 400
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w,h,x,y))
        self.resizable(False,False)
        self.configure(background="#5A5352")



app=App()
Inicio(app)
app.mainloop()