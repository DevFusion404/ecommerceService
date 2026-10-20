"""
Pricing Engine - Calculates container volumes and custom packaging specs.
"""

def calculate_cylinder_volume(radius, height):
    return 3.14159 * radius * radius * height

def get_standard_packaging_volume():
    return calculate_cylinder_volume(5.0, 10.0)

if __name__ == "__main__":
    print("Standard volume:", get_standard_packaging_volume())
