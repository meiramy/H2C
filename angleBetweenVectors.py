import math

u =(6, 5)
v = (-4,8)

def dot_product(u,v):
    dot = (u[0]*v[0]) + (u[1]*v[1])
    return dot

def magnitude(u):
    u = math.sqrt((u[0]**2) + (u[1]**2))
    return u

def magnitude(v):
    v = math.sqrt((v[0]**2) + (v[1]**2))
    return v


def angle(u,v):
    radians = math.acos(dot_product(u,v) / (magnitude(u) * magnitude(v)))
    return radians

print("u = ",u)
print("v = ",v)
print()
print("u * v = ",dot_product(u,v))
print("|u| = ",magnitude(u))
print("|v| = ", magnitude(v))
print("θ = ",angle(u,v)," = ", math.degrees(angle(u,v)), "°")
