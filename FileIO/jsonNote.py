import json

with open("jsonNote.json", "r") as file:
	fj = json.loads(file.read())
	print(len(fj))

	for i in fj:
		print(i['username'])