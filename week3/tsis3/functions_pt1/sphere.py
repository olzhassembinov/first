import math

def sphere_volume(radius):
    if radius < 0:
        return "Radius cannot be negative"
    
    # Compute the volume of the sphere
    volume = (4 / 3) * math.pi * radius**3
    
    return volume

# Test cases
print(sphere_volume(5))