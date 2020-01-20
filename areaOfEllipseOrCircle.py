import math

def area_of_ellipse(r, e = None):
    if e == None:
        e = r
    a = r * e * math.pi
    return a
    

print("Area of circle (r= 8):",area_of_ellipse(8))
print("Area of ellipse (a=4, b=3):", area_of_ellipse(4,3))
