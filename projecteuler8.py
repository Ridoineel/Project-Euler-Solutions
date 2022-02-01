import math
from utils.functions import getData

def maxThirteenProd(seq):
	MAX = 0

	for i in range(len(seq) - 12):
		sub_seq = seq[i:i + 13]

		prod = math.prod(sub_seq)

		if prod > MAX:
			MAX = prod

	return MAX

def getData(file_path):
	file = open(file_path, "r")

	return "".join(file.readlines())


def main():
	digits = getData("data/data.txt")
	digits = digits.replace("\n", "")

	# split by 0
	seq_digits = digits.split("0")

	# filter length >= 13
	seq_digits = [x for x in seq_digits if len(x) >= 13]

	MAX = 0

	for seq in seq_digits:
		maxProd = maxThirteenProd(list(map(int, seq)))

		if maxProd > MAX :
			MAX = maxProd

	print(MAX)

if __name__ == "__main__":
	main()