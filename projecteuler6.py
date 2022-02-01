# Find the difference between the sum of the squares of 
# the first one hundred natural numbers and the square of the sum.

def main():
    n = 100
    
    # square_of_sum = (1 + 2 + ... + n)^2
    square_of_sum = int(n*(n + 1)/2)**2
    
    # sum_of_squares 1^2 + 2^2 + ... + n^2
    sum_of_squares = sum(map(lambda x: x**2, range(n+1)))
    
    diff = square_of_sum - sum_of_squares

    print(diff) # 25164150

if __name__ == "__main__":
    main()
