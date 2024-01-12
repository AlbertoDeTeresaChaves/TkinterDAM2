import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):

 def __init__(self, main_window):
    super().__init__(main_window)
    main_window.title("Posicionar elementos en Tcl/Tk")
    main_window.configure(width=600,height=400)
    self.entry = ttk.Entry(self)
    self.entry.pack()

    self.button = ttk.Button(self, text="Hola, mundo!")
    self.button.pack()

    self.pack()

#MAIN     
principal = tk.Tk()
app = Application(principal)
app.mainloop()