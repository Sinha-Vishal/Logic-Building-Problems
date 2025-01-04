# Program to calculate distance between two points
# You are given two coordinates (x1, y1) and (x2, y2) of a two-dimensional graph. Find the distance between them.

# Examples: 

# Input : x1, y1 = (3, 4)
#         x2, y2 = (7, 7)
# Output : 5

# Input : x1, y1 = (3, 4) 
#         x2, y2 = (4, 3)
# Output : 1.41421

# Method 1: Without using the inbuilt library
def distance(x1, x2, y1, y2):
    dis = round((((x2 - x1)**2 + (y2 - y1)**2)**0.5), 5)
    print(f"Distance between two points is {dis}")
    return

# Method 2: Using the inbuilt library
import math
def distance_inbuit_fun(x1, x2, y1, y2):
    dis = round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0), 5)
    print(f"Distance between two points is {dis}")
    return    

if __name__ == "__main__":
    x1 = int(input())
    x2 = int(input())
    y1= int(input())
    y2 = int(input())
    distance(x1, x2, y1, y2)
    distance_inbuit_fun(x1, x2, y1, y2)