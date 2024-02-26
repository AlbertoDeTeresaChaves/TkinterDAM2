import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.base()
        self.contenido()
        
    def contenido(self):
        #NOMBRE
        self.lNombre = tk.Label(self,text="Nombre: ").grid(column=0,row=0)
        self.vNombre=tk.StringVar()
        self.tNombre = tk.Entry(self,textvariable=self.vNombre,width=10)
        self.tNombre.grid(column=1,row=0)
        
        #APELLIDO
        self.lApellido = tk.Label(self,text="Apellido: ").grid(column=2,row=0)
        self.vApellido=tk.StringVar()
        self.tApellido = tk.Entry(self,textvariable=self.vApellido,width=10)
        self.tApellido.grid(column=3,row=0)
        
        #JOB
        self.lJob = tk.Label(self,text="Job: ").grid(column=4,row=0)
        self.vJob=tk.StringVar()
        self.tJob = tk.Entry(self,textvariable=self.vJob,width=10)
        self.tJob.grid(column=5,row=0)
        
        #MGR
        self.lMGR = tk.Label(self,text="MGR: ").grid(column=6,row=0)
        self.vMGR=tk.StringVar()
        jefes=("JHON","KATIE","VANESH")
        self.tMGR = ttk.Combobox(self,values=jefes,textvariable=self.vMGR,state="readonly",width=10)
        self.tMGR.grid(column=7,row=0)
        
        #SAL
        self.lSAL= tk.Label(self,text="SAL: ").grid(column=8,row=0)
        self.vSAL=tk.DoubleVar()
        self.tSAL= ttk.Entry(self,textvariable=self.vSAL,width=10)
        self.tSAL.grid(column=9,row=0)
        
        #COM
        self.lCOM = tk.Label(self,text="COMM: ").grid(column=10,row=0)
        self.vCOM=tk.DoubleVar()
        self.tCOM = ttk.Entry(self,textvariable=self.vCOM,width=10)
        self.tCOM.grid(column=11,row=0)
        
        #DEPTNO
        self.lDEPTNO= tk.Label(self,text="DEPTNO: ").grid(column=12,row=0)
        self.vDEPTNO=tk.StringVar()
        departamentos=("BBVA","HNOS JHON","NIKE")
        self.tDEPTNO = ttk.Combobox(self,values=departamentos,textvariable=self.vDEPTNO,state="readonly",width=10)
        self.tDEPTNO.grid(column=13,row=0)
        
        #BOTON
        self.bAgregar=tk.Button(self,text="AGREGAR",command=self.añadir)
        self.bAgregar.grid(column=14,row=0)
    def añadir(self):
        empleado = (self.vNombre.get(),self.vApellido.get(),self.vJob.get(),self.vMGR.get(),self.vSAL.get(),self.vCOM.get(),self.vDEPTNO.get())
        print(empleado)
        self.vNombre=""
        self.vApellido=""
        self.vJob=""
        self.vMGR=""
        self.vSAL=""
        self.vCOM=""
        self.vDEPTNO=""

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