def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

def totient(n):
    result = n

    for i in range(2, n+1):
        if(n%i==0):
            while(n%i==0):
                n//=i
            result*=(1-1/i)
    if n>1:
        result*=(1-1/n)
    return int(result)

def modified(a,b,m):
    tot = totient(m)

    remainder = b%tot

    answer = (a**remainder)%m

    return answer

print(modified(2, 1000, 17))