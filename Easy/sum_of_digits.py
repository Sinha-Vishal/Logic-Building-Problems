# Program for Sum of Digits of a Number
# Given a number n, find the sum of its digits.

# Examples : 

# Input: n = 687
# Output: 21
# Explanation: The sum of its digits are: 6 + 8 + 7 = 21


# Input: n = 12
# Output: 3
# Explanation: The sum of its digits are: 1 + 2 = 3
def sumOfDigitsRecur(n, current_sum=0):
    if n == 0:
        print(f"Recursive Approach:\nSum = {current_sum}")
        return
    
    current_sum += n % 10
    sumOfDigitsRecur(n//10, current_sum) 
    
def sumOfDigits(n):
    sum = 0
    while n!= 0:
        rem = n%10
        sum += rem
        n = n//10
    print(f"Iterative Approach:\nSum = {sum}")

if __name__ == "__main__":
    num = int(input())
    sumOfDigits(num)
    sumOfDigitsRecur(num)