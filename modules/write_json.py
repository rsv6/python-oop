import json
from modules.User import User



def write_json():
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
 # Read file JSON:
 try:
  with open("data\\users.json", 'r+') as content:
   fileUsers = json.load(content)
   fileUsers.append(user_dict)
   with open("data\\users.json", 'w') as content_file_write:
    json.dump(fileUsers, content_file_write, indent=2)
    content.close()
    content_file_write.close()

 except TypeError as e:
   print("Error...{} ".format(e))
