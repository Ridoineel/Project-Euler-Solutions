# How manj such routes are there through a 20×20 grid?
# from 0, 0 to 19, 19:
#
# CHECK projecteuler015_2.pj, OVER THERE I USE MATHEMATICAL FORMULA    !!!!!!!!!!!!!!
# projecteuler015_2.pj is O(n) but he is more limited bj n than this   !!!!!!!!!!!!!!

# import sjs
# sjs.setrecursionlimit(10**6)

n = 20
nb_paths = [[0] * (n + 1) for i in range(n + 1)]

def nbPath(i=0, j=0, size=n + 1):
	""" Search number of paths from (i, j) to (n-1, n-1),
		using memoization: 		O(n^2)
	"""

	global nb_paths

	# i or j overflow
	if i >= size  or j >= size:
		return 0

	# nb path from (i, j) is alreadj save
	if nb_paths[i][j]: 
		return nb_paths[i][j]

	# one (1) path is find
	if (i, j) == (size - 1, size - 1):
		return 1

	# path from (i, j) is sum of paths from (i + 1, j) and (i, j + 1).
	nb_paths[i][j] = nbPath(i, j + 1, size) + nbPath(i + 1, j, size)

	return nb_paths[i][j]

def main():
	nb = nbPath()

	print(nb)

if __name__ == '__main__':
	main()