# Program to add two fractions
# Add two fraction a/b and c/d and print answer in simplest form.

# Examples : 
# Input:  1/2 + 3/2
# Output: 2/1

# Input:  1/3 + 3/9
# Output: 2/3

# Input:  1/5 + 3/15
# Output: 2/5

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def lowest(den3, num3):
    common_factor = gcd(num3, den3)
    
    den3 = int(den3 / common_factor)
    num3 = int(num3 / common_factor)
    print(num3, "/", den3)
    
def addFraction(num1, den1, num2, den2):
    den3 = gcd(den1, den2)
    den3 = (den1 * den2) / den3
    
    num3 = ((num1) * (den3 / den1) + (num2) * (den3 / den2))
    
    lowest(den3, num3)
    
    
if __name__ == "__main__":
    num1 = int(input())
    den1 = int(input())
    num2 = int(input())
    den2 = int(input())
    
    print(num1, "/", den1, " + ", num2, "/", den2, " is equal to ", end="")
    addFraction(num1, den1, num2, den2) 