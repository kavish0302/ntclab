def isPrime(p):
    if p <= 1: 
        return False
    for i in range(2, p):
        if p % i == 0: 
            return False
    return True

def divisible(a, p):
    if a % p == 0:
        return True 

def fermats(a, p):
    if isPrime(p):
        if not divisible(a, p): 
            return (a ** (p - 1)) % p == 1
        else:
            return False 
    else:
        return False

# Example usage
print(fermats(7, 19)) 
