def extendedEuclidean(a, b):
    if(b==0):
        return a, 1, 0
    
    gcd, x1, y1 = extendedEuclidean(b, a%b)
    x = y1
    y = x1-(a//b)*y1

    return gcd, x, y

def diophantineSolver(a, b, c):

    gcd, x, y = extendedEuclidean(a, b)

    if(c%gcd !=0):
        print("No value")
        return None
    
    x = x*(c//gcd)
    y = y*(c//gcd)

    return x,y


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

x, y = diophantineSolver(a, b, c)
print(f"Value of x is: {x}, Value of y is: {y}")