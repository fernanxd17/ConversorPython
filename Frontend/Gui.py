from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from Facade import Facade


class Gui(Tk):
  		
	fcd = Facade.Facade()

	def __init__(self):
		super(Gui,self).__init__()
		self.iniciar()		
		mainloop()
		#self.fcd.saludar()
		
	def iniciar(self):
		print("hola Iniciar")
		self.title ("Conversor FREE")
		self.minsize(340,100)

		self.frame = ttk.Frame(self)
		self.frame.grid(column=0, row=1, padx=20, pady=20)
		self.labelFrame = ttk.LabelFrame(self.frame, text="Selecciona tu archivo")
		self.labelFrame.grid(column=1, row=2)
		self.button()
		self.menu()
		self.convertir()
		
	
			
	def button(self):
		self.button = ttk.Button(self.labelFrame, text = "Busca tu archivo", command= self.filedialog)  #con command esta llamando un metodo en especifico
		self.button.grid(column=1,row=1)
		print("hola button")


	def filedialog(self):
		self.filename = filedialog.askopenfilename(initialdir ="/", title="Selecciona un archivo", filetype=(("docx","*.docx"),("odt","*.odt"),("xlsx","*.xlsx"),("ods","*.ods"),("pptx","*.pptx"),("odp","*.odp")))
		self.label = ttk.Label(self.labelFrame, text="")
		self.label.grid(column =1, row =2)
		self.label.configure(text= self.filename)  #self.filename me trae la ruta del documento
 	

	def menu(self):
		
		self.label = ttk.Label(self.frame,text="¿A que extencion desea convertir?")
		self.label.grid(column=1, row=3, pady=10, padx=5)
		self.comboFinal=ttk.Combobox(self.frame)
		self.comboFinal.grid(column=2, row =3)
		self.comboFinal['values'] = ('docx','odt','xlsx','ods','pptx','odp')
		self.comboFinal.current(1)
		
	def convertir(self):
		self.button = ttk.Button(self.frame, text = "Convertir archivo", command=self.convertirArchivos)  #con command esta llamando un metodo en especifico
		self.button.grid(column=1,row=6, pady=10, padx=30)
		print("hola convertir")

	def convertirArchivos(self):
	    #self.fcd.saludar()
	    #print(self.filename)
		#print(self.comboOrigen.get())
		#print(self.comboFinal.get())
		#print(self.texto.get())
		print("hola")
		self.fcd.convertFile(self.comboFinal.get(), self.filename)
		#self.fcd.convertFile('odt','C:/Users/Romero/Desktop/Proyecto/prueba.docx')
		
