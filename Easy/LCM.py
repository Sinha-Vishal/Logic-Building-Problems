# Program to find LCM of two numbers
# LCM of two numbers is the smallest number which can be divided by both numbers. 

# Input :  a = 12, b = 18
# Output :  36
# 36 is the smallest number divisible by both 12 and 18


# Input :  a = 5, b = 11
# Output :  55
# 55 is the smallest number divisible by both 5 and 11

# LCM using GCD/HCF
def gcd(a, b):
    while (a > 0 and b > 0):
        if (a > b):
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    return a

def lcm(a, b):
    lcm = (a * b) // gcd(a, b)
    return lcm

# LCM using conditional for loop
def LCM(a, b):
    greater = max(a, b)
    smaller = min(a, b)
    
    for i in range(greater, a*b+1, greater):
        if i % smaller == 0:
            return i

if __name__ == '__main__':
    a = 15
    b = 20
    print(f"LCM of {a} and {b} is {lcm(a, b)}")
    
    print(f"LCM of {a} and {b} is {LCM(a, b)}")
    