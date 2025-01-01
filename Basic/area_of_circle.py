# Problem: Program to find area of a circle
# Given the radius r. Find the area of a circle. 
# The area of the circle should be correct up to 5 decimal places.

# Examples:

# Input: r = 5
# Output: 78.53982
# Explanation: As area = PI * r * r = 3.14159265358979323846 * 5 * 5 = 78.53982, 
# as we only keep 5 digits after decimal.


# Input: r = 2
# Output: 12.56637
# Explanation: As area = PI * r * r = 3.14159265358979323846 * 2 * 2 = 12.56637, 
# as we only keep 5 digits after decimal.
import math

def findArea(r):
    return math.pi * r * r

if __name__ == "__main__":
    r = int(input())
    area = round(findArea(r), 5)
    print(f"Area of Circle = {area}")