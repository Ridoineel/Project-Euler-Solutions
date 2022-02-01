# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def isPrime(n):
    for i in range(2, int(n**.5)+1):
        if not n % i:
            return False
            
    return True

def main():
    n = 600851475143
    
    for i in range(int(n**.5), 1, -1):
        if not n % i and isPrime(i):
            print(i) # 6857
            break
    

if __name__ == "__main__":
    main()
