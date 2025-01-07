# Find if two rectangles overlap
# Given two rectangles, find if the given two rectangles overlap or not.
# Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates. 
# l1: Top Left coordinate of first rectangle. 
# r1: Bottom Right coordinate of first rectangle. 
# l2: Top Left coordinate of second rectangle. 
# r2: Bottom Right coordinate of second rectangle.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def do_overlap(l1, r1, l2, r2):
    # If one rectangle is to the left of the other
    if l1.x > r2.x or l2.x > r1.x:
        return False
    
    # If one rectangle is above the other
    if r1.y > l2.y or r2.y > l1.y:
        return False

    return True
    
# Main code
if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)
    
    if do_overlap(l1, r1, l2, r2):
        print("Rectangle Overlap")
    else:
        print("Rectangle Don't Overlap")