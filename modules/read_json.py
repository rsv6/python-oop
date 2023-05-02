import json

def read_json():
 with open("data\\users.json", 'r') as content:
		file_obj = json.load(content)
		return json.dumps(file_obj, indent=2)