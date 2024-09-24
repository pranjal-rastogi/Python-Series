import math


def circle_stats(radius):
    area = format(math.pi * radius**2, ".2f")
    circumference = format(2 * math.pi * radius, ".2f")
    return area, circumference


area, circumference = circle_stats(3)
print("Area:", area, "Circumference:", circumference)
