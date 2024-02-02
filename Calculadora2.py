from tkinter import *
from tkinter import messagebox

class Calculadora(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.grid()
        self.botones()

    def botones(self):
        estilo = {"font":("Arial",16),"bg":"white","fg":'red',"highlightbackground":'red'}
        estilo1 = {"font":("Arial",14),"bg":"white","fg":'black',"highlightbackground":'white'}

        self.display=Entry(self,font=("Arial",24),relief=RIDGE, justify=RIGHT,bg='darkblue',fg='red',borderwidth=0)
        self.display.insert(0,"0")
        self.display.grid(row=0,column=0,columnspan=4,sticky="nsew")

        lista =[
            {"text":"CE","estilo":estilo,"funcion":self.remplazarTexto,"row":1,"column":0,"par":"0"},
            {"text":"Del","estilo":estilo,"funcion":self.borrarUltimoCaracter,"row":1,"column":1,"par":""},
            {"text":"1/x","estilo":estilo,"funcion":self.inversa,"row":1,"column":2,"par":""},
            {"text":"0","estilo":estilo1,"funcion":self.añadir,"row":5,"column":1,"par":"0"},
            {"text":"1","estilo":estilo1,"funcion":self.añadir,"row":4,"column":0,"par":"1"},
            {"text":"2","estilo":estilo1,"funcion":self.añadir,"row":4,"column":1,"par":"2"},
            {"text":"3","estilo":estilo1,"funcion":self.añadir,"row":4,"column":2,"par":"3"},
            {"text":"4","estilo":estilo1,"funcion":self.añadir,"row":3,"column":0,"par":"4"},
            {"text":"5","estilo":estilo1,"funcion":self.añadir,"row":3,"column":1,"par":"5"},
            {"text":"6","estilo":estilo1,"funcion":self.añadir,"row":3,"column":2,"par":"6"},
            {"text":"7","estilo":estilo1,"funcion":self.añadir,"row":2,"column":0,"par":"7"},
            {"text":"8","estilo":estilo1,"funcion":self.añadir,"row":2,"column":1,"par":"8"},
            {"text":"9","estilo":estilo1,"funcion":self.añadir,"row":2,"column":2,"par":"9"},
            {"text":"/","estilo":estilo,"funcion":self.añadir,"row":1,"column":3,"par":"/"},
            {"text":"*","estilo":estilo,"funcion":self.añadir,"row":2,"column":3,"par":"*"},
            {"text":"-","estilo":estilo,"funcion":self.añadir,"row":3,"column":3,"par":"-"},
            {"text":"+","estilo":estilo,"funcion":self.añadir,"row":4,"column":3,"par":"+"},
            {"text":"+/-","estilo":estilo,"funcion":self.cambioSigno,"row":5,"column":0,"par":""},
            {"text":".","estilo":estilo,"funcion":self.añadir,"row":5,"column":2,"par":"."},
            {"text":"=","estilo":estilo,"funcion":self.evaluar,"row":5,"column":3,"par":""}]

        for a in lista:
            nuevo_Boton(self,a)

class nuevo_Boton(Button):
    def __init__(self,v,a):
        super().__init__(v)
        f=a["funcion"]
        Button(v,a["estilo"],text=a["texto"],command=lambda :f(a["par"])).grid(row=a["row"],column=a["column"],sticky="nsew")  

    def remplazarTexto(self,texto):
        self.display.delete(0,END)
        self.display.insert(0,texto)

    def añadir(self,texto):
        actualTexto = self.display.get()
        textLength = len(actualTexto)
        if(actualTexto =="0"):
            self.remplazarTexto(texto)
        else:
            self.display.insert(textLength,texto)    

    def evaluar(self):
        try:
            self.remplazarTexto(eval(self.display.get()))
        except (SystemError, AttributeError):
            messagebox.showerror("ERROR","Syntax Error")
            self.remplazarTexto("0")
        except ZeroDivisionError:
            messagebox.showerror("ERROR","Cannot divide by 0")
            self.remplazarTexto("0")

    def contieneSigno(self):
        lista=["/","*","+","-"]
        display = self.display.get()
        for c in display:
            if c in lista:
                return True
        return False
    
    def cambioSigno(self):
        if self.contieneSigno():
            self.evaluar()
        firstChat = self.display.get()[0]
        if firstChat =="0":
            pass
        elif firstChat == "-":
            self.display.delete(0)
        else:
            self.display.insert(0,"-")

    def inversa(self):
        self.display.insert(0,"1/(")
        self.añadir(")")
        self.evaluar()

    def borrarUltimoCaracter(self):
        textLength = len(self.display.get())
        if textLength >=1:
            self.display.delete(textLength - 1,END)
        elif textLength == 1:
            self.remplazarTexto("0")
class App(Tk):
    def __init__(self):
        super().__init__()
        self.configure(padx=30,pady=30)
        self.title("Calculadora")
        w = 425
        h = 300
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w,h,x,y))
        self.resizable(False,False)

app = App()
Calculadora(app)
app.mainloop()
