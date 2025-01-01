# Problem: Swap Two Numbers
# Given two numbers a and b, the task is to swap them.

# Examples:

# Input: a = 2, b = 3
# Output: a = 3, b = 2

# Input: a = 20, b = 0
# Output: a = 0, b = 20

# Input: a = 10, b = 10
# Output: a = 10, b = 10 

def swapNumbers(a, b):
    print(f"Before swapping a = {a} b = {b}")
    a, b = b, a
    print(f"After swapping a = {a} b = {b}")
    
    
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    swapNumbers(a, b)