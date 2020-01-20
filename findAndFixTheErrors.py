import math


def circle_area(radius):
    radius_squared = radius ** 2
    area = math.pi * radius_squared
    return area

def cone_slant_height(radius,height):
    slant = math.sqrt(radius * radius + height * height)
    return slant

def cone_lateral_surface_area(radius,height):
    s = cone_slant_height(radius,height)
    L = math.pi * radius * s
    return L

def cone_surface_area(radius,height):
    s = cone_slant_height(radius,height)
    area = math.pi * radius * s + math.pi * (radius**2)
    return area

def cone_volume(radius,height):
    area_of_base = circle_area(radius)
    volume = (1/3) * area_of_base * height
    return volume

def main():
    try:
        print("Welcome to the cone Calculator")
        print("===============================")
        print()
    
        radius = float(input("Enter the radius of the base: "))
        height = float(input("Enter the height of the cone: "))
    
        print()
        print("Base radius           r = ",radius)
        print("Cone height           h = ",height)
        print("Slant height          s = ",cone_slant_height(radius,height))
        print("Volume                V = ",cone_volume(radius,height))
        print("Lateral surface area  L = ",cone_lateral_surface_area(radius,height))
        print("Base surface area     B = ",circle_area(radius))
        print("Total surface area    A = ",cone_surface_area(radius,height))

    except Exception:
        print("Invalid value")


if __name__ == "__main__":
    main()
