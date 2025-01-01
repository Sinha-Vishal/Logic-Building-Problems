# Problem: Program to find sum of first n natural numbers
# Examples : 

# Input: n = 3
# Output: 6
# Explanation: Note that 1 + 2 + 3 = 6

# Input  : 5
# Output : 15 
# Explanation : Note that 1 + 2 + 3 + 4 + 5 = 15

def findSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

if __name__ == "__main__":
    n = int(input())
    print(findSum(n))
        