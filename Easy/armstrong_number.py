# Program for Armstrong Numbers
# Given a number x, determine whether the given number is Armstrong’s number or not.

# Input:153
# Output: Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153


# Input: 120
# Output: No
# 120 is not a Armstrong number.
# 1*1*1 + 2*2*2 + 0*0*0 = 9


# Input: 1253
# Output: No
# 1253 is not a Armstrong Number
# 1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723


# Input: 1634
# Output: Yes
# 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
def order(x):
    n = 0
    while(x != 0):
        n = n+1
        x = x//10
    return n

def isArmstrong(x):
    n = order(x)
    temp = x
    sum = 0
    while(temp != 0):
        r = temp % 10
        sum += pow(r,n)
        temp //= 10
        
    return (sum == x)

print(isArmstrong(153))