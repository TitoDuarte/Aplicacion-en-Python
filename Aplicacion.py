from tkinter import ttk
from tkinter import *
import math
import datetime
class Desk:
    def __init__(self, window):
      
        Ancho = 500
        Alto = 250
         self.wind = window

        
        self.wind.geometry(str(ancho)+'x'+str(alto))

        self.wind.columnconfigure(0, weight=1)
        self.wind.title('Examen Final')
        

        frame = LabelFrame(self.wind, text = 'Bienvenido')
        frame.grid(row = 0, column = 0, columnspan = 5, pady = 20)      
        
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
       
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, columnspan = 6)

        Label(frame, text = 'Apellido: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, columnspan = 6)

        Label(frame, text = 'Dia: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, columnspan = 6)

        Label(frame, text = 'Mes: ').grid(row = 4, column = 0)
        self.var4 = Entry(frame)
        self.var4.grid(row = 4, columnspan = 6)

        Label(frame, text = 'Año: ').grid(row = 5, column = 0)
        self.var5 = Entry(frame)
        self.var5.grid(row = 5, columnspan = 6)
        
