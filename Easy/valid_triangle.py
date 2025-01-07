# Check whether triangle is valid or not if sides are given

# Given three sides, check whether triangle is valid or not. 
# Examples:

# Input :  a = 7, b = 10, c = 5 
# Output : Valid

# Input : a = 1 b = 10 c = 12 
# Output : Invalid

def isvalidTriangle(a, b, c):
    if (a + b) > c and (b + c) > a and (c + a) > b:
        return "Valid"
    else:
        return "Invalid"
    
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(isvalidTriangle(a, b, c))