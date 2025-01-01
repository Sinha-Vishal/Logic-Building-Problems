# Problem: Program for sum of geometric series
# A Geometric series is a series with a constant ratio between successive terms. 
# The first term of the series is denoted by a and common ratio is denoted by r. 
# The series looks like this :- a, ar, ar2, ar3, ar4, . . .. 
# The task is to find the sum of such a series. Examples :

# Input : a = 1
#         r = 0.5
#         n = 10
# Output : 1.99805

# Input : a = 2
#         r = 2
#         n = 15
# Output : 65534

def sumOfGP(a, r, n):
    sum = 0
    i = 0
    while i < n:
        sum = sum + a
        a = a * r
        i = i + 1
    return sum

if __name__ == "__main__":
    a = int(input())
    r = float(input())
    n = int(input())
    print(round(sumOfGP(a, r, n), 5))