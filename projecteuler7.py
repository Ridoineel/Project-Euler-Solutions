def isPrime(n):
    for i in range(2, int(n**.5)+1):
        if not n % i:
            return False
            
    return True
    
def main():
    n = 10001
    
    count = 0
    i = 1
    
    while count < n:
        i += 1
        count += isPrime(i)

    print(i) # 104743

if __name__ == "__main__":
    main()
