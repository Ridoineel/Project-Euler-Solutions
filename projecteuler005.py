# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def pgcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
    
def ppcm(a, b):
    return (a*b) // pgcd(a, b)

def smallest(n):
    if n == 1:
        return 1

    return  ppcm(n, smallest(n-1))
    
def main():
    n = 20
    print(smallest(n)) # 232792560

if __name__ == "__main__":
    main()
