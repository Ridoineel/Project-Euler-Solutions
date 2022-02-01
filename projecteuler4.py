def isPalindromic(n: int):
    return str(n) == str(n)[::-1]

def main():
    pald = 0
    
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            nb = i * j
            if isPalindromic(nb):
                if pald < nb:
                    pald = nb
                break
                
    print(pald) # 906609
    
if __name__ == "__main__":
    main()