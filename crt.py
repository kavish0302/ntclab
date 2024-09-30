def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

def extended_gcd(a,b):

    if b==0:
        return a, 1, 0
    
    g, x1, y1 = extended_gcd(b, a%b)

    x = y1
    y = x1-(a//b)*y1

    return g,x,y

def inverse(a,m):

    g, x, y = extended_gcd(a,m)

    if(g!=1):
        return None
    
    return x%m

def crt(b, m):

    M = 1

    for small_m in m:
        M *=small_m

    res = 0
    for i in range(len(m)):
        Mi = M // m[i]
        inv = inverse(Mi, m[i])

        if inv is None:
            return None
        
        res += b[i]*Mi*inv

    return res%M

b = [8,3]
m = [9,20]

ans  = crt(b,m)

print(ans)