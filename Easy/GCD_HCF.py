# Program to Find GCD or HCF of Two Numbers

# Given two numbers a and b, the task is to find the GCD of the two numbers.

# Note: The GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest number that divides both of them.

# Examples:

# Input: a = 20, b = 28
# Output: 4
# Explanation: The factors of 20 are 1, 2, 4, 5, 10 and 20. The factors of 28 are 1, 2, 4, 7, 14 and 28. Among these factors, 1, 2 and 4 are the common factors of both 20 and 28. The greatest among the common factors is 4.


# Input: a = 60, b = 36
# Output: 12

# Naive Approach
def gcd(a, b):
    
    result = min(a, b)
    
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
        
    return result

# Euclidean algorithms Basic
def gcdBasic(a, b):
    if a == 0:
        return b
    
    return gcdBasic(b % a, a)

# Euclidean algorithms Extended
def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = gcdExtended(b%a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

# Iterative implementation
def gcdIterative(a, b):
    while (a > 0 and b > 0):
        if (a > b):
            a = a % b
        else:
            b = b % a
    
    if (a == 0):
        return b
    return a
        

if __name__ == '__main__':
    a = 98
    b = 56
    print(f"GCD of {a} and {b} is {gcd(a, b)}")
    
    print(f"GCD of {a} and {b} is {gcdBasic(a, b)}")
    
    g, x, y = gcdExtended(a, b)
    print(f"GCD of {a} and {b} is {g}")
    
    print(f"GCD of {a} and {b} is {gcdIterative(a, b)}")