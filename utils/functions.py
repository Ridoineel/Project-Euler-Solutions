
def nbLeapYear(start, end):
	if start > end:
		start, end = end, start

	nb_leap = 0

	if start % 4 != 0:
		# set start to next divisible by 4 (to get leap lear)
		start = 4 * (start//4 + 1) 

	for y in range(start, end + 1, 4):
		if y % 400 == 0 or y % 100 != 0:
			nb_leap += 1

	return int(nb_leap)

def isLeapYear(year):
	return year%400 == 0 or (year%4 == 0 and year%100 != 0)