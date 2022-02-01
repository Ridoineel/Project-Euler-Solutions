def main():
    lim = 1000
    lim -= 1
    
    # Last multiple of 3, 5 and 15 bellow or equal to lim
    lim3 = (lim//3) * 3
    lim5 = (lim//5) * 5
    lim15 = (lim//15) * 15
    
    # Sum of multiples of 3, 5 and 15 bellow or equal to lim
    S3 = lim3 * (lim3/3 + 1)/2
    S5 = lim5 * (lim5/5 + 1)/2
    S15 = lim15 * (lim15/15 + 1)/2
    
    # Total sum
    _sum = S3 + S5 - S15
    
    print(int(_sum)) # 233168
    
if __name__ == "__main__":
    main()
