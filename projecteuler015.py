# How many such routes are there through a 20×20 grid?
# from 0, 0 to 19, 19

n = 20
nb_paths = [[0] * (n + 1) for i in range(n + 1)]

def nbPath(x=0, y=0, size=n + 1):
	global nb_paths

	# x or y overflow
	if x >= size  or y >= size:
		return 0

	# nb path on (x, y) is already save
	if nb_paths[x][y]: 
		return nb_paths[x][y]

	# one (1) path is find
	if (x, y) == (size - 1, size - 1):
		return 1

	# path from (x, y) is sum of paths from (x + 1, y) and (x, y + 1).
	nb_paths[x][y] = nbPath(x, y + 1) + nbPath(x + 1, y)

	return nb_paths[x][y]

def main():
	nb = nbPath()

	# for i in nb_paths: print(*i)

	print(nb)

if __name__ == '__main__':
	main()