# Problem: Program to Check Arithmetic Progression
# A sequence of numbers is called an Arithmetic progression 
# if the difference between any two consecutive terms is always the same.
# Example: 

# Sequence 1, 4, 7,10 is an AP because the difference between any 
# two consecutive terms in the series (common difference) is the same.


# The difference between 2nd and 1st term 4 – 1 = 3
# The difference between 3rd and 2nd term 7 – 4 = 3
# The difference between 4th and 3rd term 10 – 7 = 3

def checkIsAP(arr, n):
    if (n == 1):
        return True
    arr.sort()
    
    d = arr[1] - arr[0]
    for i in range(2, n):
        if (arr[i] - arr[i -1] != d):
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    arr = []
    i = 1
    while i <= n:
        arr.append(int(input()))
        i += 1
    print(checkIsAP(arr, n))
        