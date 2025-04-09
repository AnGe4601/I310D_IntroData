import math

def calculate_volume_of_sphere(radius):
    v = (4/3) * (math.pi) * (radius ** 3)
    return v

print(calculate_volume_of_sphere(30))
print(calculate_volume_of_sphere(40))
