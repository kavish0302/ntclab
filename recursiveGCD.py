
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)

a = 33
b = 21

a = int(input("Enter value of a: "))
print("\n")
b = int(input("Enter value of b: "))

print(f"Gcd of a and b is: {gcd(a,b)}")
