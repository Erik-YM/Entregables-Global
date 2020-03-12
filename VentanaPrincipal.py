from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit, QLabel, QWidget, QComboBox, QRadioButton, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize

import sys
###############################

from Memento import *
from tkinter import *

class MDIWindow(QMainWindow):
    AutoOriginal = AutoOriginal("white")
    caretaker = Caretaker(AutoOriginal)
    cc = 0
    ci = 0
    cn = 0
    pos = 0
    root = Tk()
    root.title('canvas')
    count = 0
    countProxy = 0
    countState = 0
    countBuilder= 0
    canvas = Canvas(width=220, height=110, bg='white')
    canvas.pack(side = TOP, expand = True, fill = BOTH)
    def __init__(self):
        super().__init__()
        
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        bar = self.menuBar()
        file = bar.addMenu("Patrones")
        file.addAction("Patron Memento")

        bel = QLabel(self)
        imagen = QPixmap('./imagenes/logoUniversidad.png')
        bel.setPixmap(imagen)
        bel.setGeometry(400,20,400,400)
        self.mdi.setStyleSheet("background-color: rgb(240, 240, 240);")
        file.triggered[QAction].connect(self.WindowTrig)
        self.setWindowTitle("Pantalla Principal")


        
        
    def WindowTrig(self, p):
 
#=====================================================================================================================================================================

        if p.text() == "Patron Memento":
            subState = QMdiSubWindow()
            subState.resize(400,400)

            widgetState = QWidget()
            
            self.layoutState = QGridLayout(widgetState)
            self.layoutState.setContentsMargins(0,0,0,0)
            self.layoutState.setObjectName("gridState")

            labelEstado = QLabel()
            labelEstado.setText("Memento")
            self.layoutState.addWidget(labelEstado,0,1,1,1)

            self.comboEstado = QComboBox()
            self.comboEstado.addItem("blue")
            self.comboEstado.addItem("yellow")
            self.comboEstado.addItem("red")
            self.comboEstado.addItem("green")
            self.layoutState.addWidget(self.comboEstado,0,2,1,1)

            btnanterior = QPushButton('Color Anterior')
            self.layoutState.addWidget(btnanterior,1,2,1,1)
            btnanterior.clicked.connect(self.button_anterior)

            btnnext = QPushButton('Color Siguiente')
            self.layoutState.addWidget(btnnext,1,4,1,1)
            btnnext.clicked.connect(self.button_next)
            
            btnver = QPushButton('Ver')
            self.layoutState.addWidget(btnver,1,6,1,1)
            btnver.clicked.connect(self.button_ver)
            

            subState.setWidget(widgetState)
            subState.setWindowTitle("Patrón Memento")
            self.mdi.addSubWindow(subState)
            subState.show()
################################
    def button_anterior(self):
        #self.ci = self.ci+1
        #self.cn = 0
        self.pos = self.pos-1
        print(self.ci)

        if self.cc == 0:
            print('No existe un anterior')
        else:


            
            if (self.pos) >= 0:
                color = self.caretaker.undo(self.pos)
                
                self.canvas.create_rectangle(10, 20, 130, 80, width=1, fill=color)
                self.canvas.create_rectangle(40, 10, 100, 80, width=1, fill=color)
                self.canvas.create_rectangle(90, 20, 70, 40, width=1, fill="white")
                #self.canvas.create_oval(10, 10, 30, 30, width=5, fill='black')
                #self.canvas.create_oval(10, 90, 30, 60, width=1, fill='black')
                self.root.mainloop()                
                
                

            else:
                print('No se puede retroceder más ')
                

        
 ################################
    def button_next(self):
        #self.cn += 1
        #self.ci = 0
        
        
        print(self.pos)

        #if self.pos != self.cc:
            

        if self.pos >= self.cc  :
            
            
            print('No existe uno siguiente')
        else:
           
            color = self.caretaker.siguiente(self.pos)
            self.canvas.create_rectangle(10, 20, 130, 80, width=1, fill=color)
            self.canvas.create_rectangle(40, 10, 100, 80, width=1, fill=color)
            self.canvas.create_rectangle(90, 20, 70, 40, width=1, fill="white")
            #self.canvas.create_oval(10, 10, 30, 30, width=5, fill='black')
            #self.canvas.create_oval(10, 90, 30, 60, width=1, fill='black')
            self.pos = self.pos+1
            self.root.mainloop()       
#############################
    def button_ver(self):
         
        self.ci = 0
        self.cn = 0
        estado = self.comboEstado.currentText()
        self.cc = self.cc+1
        self.pos = self.cc
        
        if (estado == "blue"):
            self.caretaker.backup()
            self.AutoOriginal.cambiarColor("blue")
            
            self.canvas.create_rectangle(10, 20, 130, 80, width=1, fill="blue")
            self.canvas.create_rectangle(40, 10, 100, 80, width=1, fill="blue")
            

        if (estado == "yellow"):
            self.caretaker.backup()
            self.AutoOriginal.cambiarColor("yellow")
            self.canvas.create_rectangle(10, 20, 130, 80, width=1, fill="yellow")
            self.canvas.create_rectangle(40, 10, 100, 80, width=1, fill="yellow")
                      
            
        if (estado == "red"):
            self.caretaker.backup()
            self.AutoOriginal.cambiarColor("red")
            self.canvas.create_rectangle(10, 20, 130, 80, width=1, fill="red")
            self.canvas.create_rectangle(40, 10, 100, 80, width=1, fill="red")
            

                                         
        if (estado == "green"):
            self.caretaker.backup()
            self.AutoOriginal.cambiarColor("green")
            self.canvas.create_rectangle(10, 20, 130, 80, width=1, fill="green")
            self.canvas.create_rectangle(40, 10, 100, 80, width=1, fill="green")
            
        self.canvas.create_rectangle(90, 20, 70, 40, width=1, fill="white" )    
        self.canvas.create_oval(20, 80, 40, 100, width=5, fill="black")
        self.canvas.create_oval(100, 80, 80, 100, width=1, fill="black")
        self.root.mainloop()
        
   
        
def iniciarInterfazProyecto():
    app = QApplication(sys.argv)
    mdi  = MDIWindow()
    mdi.show()
    app.exec_()     
