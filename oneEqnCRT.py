def gcd(a,b):
    if (b==0):
        return a
    return gcd(b, a%b)

def extended_gcd(a,b):
    
    if(b==0):
        return a, 1, 0
    
    g, x1, y1 = extended_gcd(b, a%b)

    x = y1
    y = x1 - (a//b)*y1

    return g, x, y

def mod_inverse(a,m):
    
    g, x, y = extended_gcd(a,m)

    if(g!=1):
        return None
    
    else:
        return x%m

def crt(a,b,m):
    g = gcd(a,m)

    if(b%g!=0):
        return None
    
    if(g!=1):
        a = a//g
        b = b//g
        m = c//g

    inv = mod_inverse(a,m)

    ans = (inv*b)%m

    return ans

a = 14
b = 12
c = 18

print(crt(a,b,c))