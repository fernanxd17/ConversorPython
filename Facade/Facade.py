from Backend import Conversor

class Facade:

	cvs =  Conversor.Conversor()
	def __init__(self):
		super(Facade, self).__init__()
		
		
	def convertFile(self,ext,ruta):
			print("hola facade")
			self.cvs.convertFile(ext,ruta)

	def saludar(self):
			print("saluldar")

