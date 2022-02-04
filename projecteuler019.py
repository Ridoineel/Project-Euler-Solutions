# How many Sundays fell on the first of the month during 
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# main2 use datetime module (with generalization)
# main use explicit algorithm

from math import ceil
import datetime

def main2(): # is not use (call) by default
	nb_sunday = 0
	year_start = 1901
	year_end = 2000

	for year in range(year_start, year_end + 1):
		for month in range(1, 13):
			if datetime.date(year, month, 1).weekday() == 6:
				nb_sunday += 1

	print(nb_sunday)

def main():
	""" Output: number of sundays fell on the first of month 
		during 1 Jan 1901 -> 31 Dec 2000

	"""

	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	nb_sundays = 0
	days_between = 100
	nb_leap_year = 25
	total_days = nb_leap_year + days_between*365

	# days_from_start = 1 for monday, 2 -> tuesday 3 -> wednesday, ..., 7 -> sunday
	days_from_start = 2 # for (1 Jan 1901)
	month_from_start = 1

	while total_days > 0:
		if days_from_start % 7 == 0:
			nb_sundays += 1

		days_to_add = days[(month_from_start - 1) % 12]

		# if month is febuary and year is leap year
		if month_from_start % 12 == 2 and ceil(month_from_start/12) % 4 == 0:
			days_to_add += 1

		days_from_start += days_to_add
		total_days -= days_to_add

		month_from_start += 1

	print(nb_sundays)

if __name__ == '__main__':
	main()