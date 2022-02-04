# Find the sum of the digits in the number 100!

from math import factorial

def main():
	n = 100

	f_n = factorial(n)
	f_n_string = str(f_n)

	S = sum(map(int, f_n_string))

	print(S)

if __name__ == '__main__':
	main()