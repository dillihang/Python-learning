def prime_numbers():
    n = 2
    while True:  
        is_prime = True 
        
        for i in range(2, n):  
            if n % i == 0:     
                is_prime = False
                break           
        
        if is_prime:
            yield n            
        
        n += 1           
     
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))