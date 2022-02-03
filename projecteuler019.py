# How many Sundays fell on the first of the month during 
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# main2 use datetime
# main use explicit algorithm

from math import ceil
import datetime

def main():
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	nb_leap = 25
	total_days = nb_leap + 100*365

	nb_sunday = 0
	nb_days = 2 # 2 for tuesday (1 jan 1901) (1 -> monday, 3 -> wednesday, ..., 7 -> sunday)
	mounth_from_start = 1

	while total_days > 0:
		if nb_days % 7 == 0:
			nb_sunday += 1

		day_to_add = days[(mounth_from_start - 1) % 12]

		# if leap year
		if mounth_from_start % 12 == 2 and ceil(mounth_from_start/12) % 4 == 0:
			day_to_add += 1

		nb_days += day_to_add
		total_days -= day_to_add

		mounth_from_start += 1

	print(nb_sunday)

def main2(): # is not use by default
	nb_sunday = 0
	year_start = 1901
	year_end = 2000

	for year in range(year_start, year_end + 1):
		for mounth in range(1, 13):
			if datetime.date(year, mounth, 1).weekday() == 6:
				nb_sunday += 1

	print(nb_sunday)


if __name__ == '__main__':
	main()