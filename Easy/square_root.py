# Square root of an integer
# Given a positive integer n, find its square root. If n is not a perfect square, then return floor of √n.

# Examples : 

# Input: n = 4
# Output: 2
# Explanation: The square root of 4 is 2.


# Input: n = 11
# Output: 3
# Explanation: The square root of 11 lies in between 3 and 4 so floor of the square root is 3.

# Naive Approach
def find_Square_Root(n):
    res = 1
    while res * res <= n:
        res += 1
        
    return res - 1

# Using Binary Search
def squar_Root(n):
    
    # Initial search
    lo = 1
    hi = n
    res = 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if mid * mid <= n:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    
    return res

# Using Build in function
import math

def floorSqrt(n):
    res = int(math.sqrt(n))
    return res

if __name__ == "__main__":
    n = int(input())
    print("Navie Approach - Square Root of", n, "is", find_Square_Root(n))
    print("Using Binary Search - Square Root of", n, "is", squar_Root(n))
    print("Using Build in function - Square Root of", n, "is", floorSqrt(n))