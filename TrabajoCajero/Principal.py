from tkinter import *

class Inicio(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(background="#5A5352")
        self.grid(column=0, row=0, padx=200, pady=10, sticky=(N, W, E, S))        
        textobold = {"foreground": "white", "background": "#5A5352", "font": "helvetica 11 bold"}
        
        Label(self, text="MONEDA", **textobold).grid(column=0, row=0, padx=10, pady=5)
        Label(self, text="CANTIDAD", **textobold).grid(column=1, row=0, padx=10, pady=5)

        monedas = ["500.00", "200.00", "100.00", "50.00", "20.00", "10.00", "5.00", "2.00", "1.00","0.50", "0.20", "0.10", "0.05", "0.02", "0.01"]

        for i, moneda in enumerate(monedas, start=1):
            Label(self, text=moneda, **textobold).grid(column=0, row=i)
            Spinbox(self, from_=0, to=100, width=10).grid(column=1, row=i)


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("CAJERO")
        w = 600
        h = 400
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False, False)
        self.configure(background="#5A5352")


app = App()
Inicio(app)
app.mainloop()