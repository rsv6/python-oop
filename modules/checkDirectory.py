import os

def checkDirectory(path_folder: str) -> None:
	try:
		access = 0o777
		os.mkdir(path_folder, access)
		print("Folder {} created successfully ".format(path_folder))
	except FileExistsError as ef:
		print("Folder already exists!")