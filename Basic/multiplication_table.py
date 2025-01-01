# Problem: Program to print multiplication table of a number
# Examples : 

# Input:  5
# Output: 
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50

def printTable(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")
        
if __name__ == "__main__":
    n = int(input())
    printTable(n)