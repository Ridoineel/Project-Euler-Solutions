def main():
	lim = 2_000_000

	marqued = [False] * lim 
	S = 2

	for i in range(3, lim, 2): # check odd number
		if not marqued[i]:
			S += i

			# marqued multiples of i
			for j in range(i, lim, i):
				marqued[j] = True

	print(S)

if __name__ == "__main__":
	main()