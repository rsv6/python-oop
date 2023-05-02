import os

from modules.checkDirectory import checkDirectory
from modules.existsFile import existsFile
from modules.read_json import read_json
from modules.write_json import write_json


if __name__ == "__main__":

	try:
		# file_path = sys.argv[1] 
		opc = int(input("Escolha uma opção:\n"+
				"1 - Criar Pasta\n"+
				"2 - Criar Arquivo JSON\n"+
				"3 - Criar Usuario\n"+
				"4 - Lista Usuarios\n"+
				"0 - Sair\n"+
		"=> "))

		if opc == 1:
			file_path = str(input("Enter name of directory: "))
			checkDirectory(os.getcwd()+"\\"+file_path)
		
		if opc == 2:
			name_file = str(input("Enter the name of the file: "))
			existsFile(os.getcwd()+"\\data", name_file)

		if opc == 3: 
			write_json()

		if opc == 4:
			users = read_json()
			print(users)

		if opc == 0:
			exit(0)


		# name_file = str(input("Enter the name of the file: "))
		# existsFile(os.getcwd()+"\\"+file_path, name_file)
			

	except IndexError as e:
		print("Args empty!")
