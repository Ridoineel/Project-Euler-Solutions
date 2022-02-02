# How many such routes are there through a 20×20 grid?
# from 0, 0 to 19, 19

from math import factorial

def nbPath(n):
	""" Search number of paths from (0, 0) to (n-1, n-1).
		With combinatorics, the methematical expression is:
		(2n!)/(n!*n!)
	"""

	A = factorial(2*n)
	B = factorial(n)**2

	return A/B

def main():
	nb = nbPath(20)

	print(nb)

if __name__ == '__main__':
	main()