
def getData(file_path):
	file = open(file_path, "r")

	return "".join(file.readlines())