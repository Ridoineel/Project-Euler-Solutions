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
