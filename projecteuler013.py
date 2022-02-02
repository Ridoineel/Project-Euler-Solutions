# Work out the first ten digits of the sum of the one-hundred 50-digit numbers in data/data013.txt.

def getData(file_path):
	file = open(file_path, "r")

	return "".join(file.readlines())

def main():
	data = getData("data/data013.txt")
	
	data = [int(i) for i in data.split()]

	S = sum(data)
	first_ten = str(S)[:10]

	print(first_ten)

if __name__ == '__main__':
	main()
