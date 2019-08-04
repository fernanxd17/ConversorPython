import subprocess


class Conversor:

	def __init__(self):
 		super(Conversor, self).__init__()

	def convertFile(self,ext, ruta):
		print(ext)
		print(ruta)

		cmd = 'soffice --convert-to ' + ext + ' '+ ruta + ' --headless' 
		print(cmd)
		subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=False)
		print("finalizo")

# 'soffice --convert-to odt C:/Users/Romero/Desktop/pueba.docx --headless'