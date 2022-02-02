# Find the maximum total from top to bottom of the triangle in data/data18.txt
# 
# Method: use memoization and add to (i, j) max of here lower neightbors
# Without memoization is very slow

def getData(file_path):
	file = open(file_path, "r")

	return "".join(file.readlines())

sum_from_ij = {}

def totalFromTop(T: [int], i=0, j=0):
	if not sum_from_ij.get((i, j)):
		if i >= len(T) or (j < 0 or j >= len(T[-1])):
			return 0
		if i == len(T) - 1:
			return T[i][j]

		sum_from_ij[i, j] = T[i][j] + max(totalFromTop(T, i + 1, j), totalFromTop(T, i + 1, j + 1))

		return sum_from_ij[i, j]

	return sum_from_ij[i, j]

def main():
	data = getData("data/data18.txt")
	data = [[int(i) for i in line.split()] for line in data.split("\n")]

	print(totalFromTop(data))

if __name__ == '__main__':
	main()