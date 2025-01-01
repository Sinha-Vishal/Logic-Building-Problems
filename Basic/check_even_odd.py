# Problem: Check if a number is even or odd
# Given a number n, check whether it is even or odd. Return true for even and false for odd.

# Examples: 
# Input: 2 
# Output: true

# Input: 5
# Output: false

def isEven(n):
    return (n % 2 == 0)

if __name__ == "__main__":
    n = int(input())
    if isEven(n):
        print("true")
    else:
        print("false")