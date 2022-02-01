def pgcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
    
def main():
    lim = 5000
    n_phi = 0, 0
    
    for n in range(2, lim + 1):
        phi = 0
        for i in range(1, n):
            phi += pgcd(i, n) == 1

        if n_phi[0] < n/phi:
            n_phi = n/phi, n
    
    print(n_phi)

if __name__ == "__main__":
    main()