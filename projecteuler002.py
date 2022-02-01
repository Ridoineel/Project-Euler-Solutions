# Sum of even fibonacci number do not exceeded four million

def evenfib(limit_value: int):
    i, j = 1, 2
    
    while i < limit_value:
        if i % 2 == 0: 
            yield i
        i, j = j, i + j
        
def main():
    lim = 4000000
    
    print(sum(evenfib(lim))) #4613732

if __name__ == "__main__":
    main()