# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def main():
	n = 2**1000
	
	SUM = sum(int(digit) for digit in str(n))

	print(SUM)

if __name__ == '__main__':
	main()