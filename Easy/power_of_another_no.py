# Check if a number is a power of another number
# Given two positive numbers x and y, check if y is a power of x or not.
# Examples : 


# Input:  x = 10, y = 1
# Output: True
# x^0 = 1


# Input:  x = 10, y = 1000
# Output: True
# x^3 = 1000


# Input:  x = 10, y = 1001
# Output: False

def isPower(x, y):
    i = 0
    while i < y:
        if x**i == y:
            return True
        else:
            i += 1
    return False

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    print(isPower(x, y))
        