import math

def polysum(n, s):
   
    a = ((0.25*n*(s**2))/(math.tan(math.pi/n)))
    p = n*s
    result = a + (p**2)   
    return round(result, 4)
print(polysum(3,4))