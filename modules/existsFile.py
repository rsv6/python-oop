import json
import os
from os.path import exists
from modules.User import User
from modules.write_json import write_json


def existsFile(path_file: str, name_file: str) -> None:
	if (os.path.exists(path_file+'\\'+name_file)):
		if  exists(path_file+"\\"+name_file):
			print("File already exists!")

			print("Adicionar novo usuario! ")
			user = User(
					input("Name: "), 
					input("Age: "),
					input("Cpf: "),
					input("Login: "),
					input("Password: "),
					input("Email: "),					
				)

			user_dict = {
				'name': user.name,
				'age': user.age,
				'cpf': user.cpf,
				'login': user.login,
				'password': user.password,
				'email': user.email,
			}



			# Read and Write file JSON:
			write_json(path_file, name_file)

			# with open(path_file+"\\"+name_file, 'r+') as content:
			# 	fileUsers = json.load(content)
			# 	fileUsers.append(user_dict)
			# 	with open(path_file+"\\"+name_file, 'w') as content_file_write:
			# 		json.dump(fileUsers, content_file_write, indent=2)
			# 		content.close()
			# 		content_file_write.close()



			## Read and write in file JSON:
			# with open(path_file+"\\"+name_file, 'r') as content:
			# 	fileUsers = json.load(content)
				
			# 	fileUsers.append(user_dict)

			# with open(path_file+"\\"+name_file, 'w') as content_file_write:
			# 	json.dump(fileUsers, content_file_write, indent=2)


	else:
		with open(path_file+"\\"+name_file, 'w+') as content:
			content.write('[]')
			print(content.read())
			print("File created!")
			content.close()