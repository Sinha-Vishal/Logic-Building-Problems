# Factorial of a Number
# Given the number n (n >=0), find its factorial. Factorial of n is defined as 1 x 2 x … x n. For n = 0, factorial is 1. We are going to discuss iterative and recursive programs in this post.

# Examples:

# Input: n = 5
# Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120


# Input: n = 4
# Output: 24
# Explanation: 4! = 4 * 3 * 2 * 1 = 24


# Input: n = 0
# Output: 1


# Input: n = 1
# Output: 1

# Iterative Solution Approach:
def factorial(n):
    res = 1
    
    for i in range(2, n + 1):
        res *= i
    
    return res

# Recursive Solution Approach:
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    num = int(input())
    print("Factorial of", num, "is", factorial(num))
    print("Factorial of", num, "is", factorial_recursive(num))