# Check for Prime Number
# You are given a number n. Check whether it is a Prime number or not.

# Input:  n = 10
# Output: false
# Explanation: 10 is divisible by 2 and 5 

# Input:  n = 11
# Output: true
# Explanation: 11 is divisible by 1 and 11 only

# Input:  n = 1
# Output: false
# Explanation: 1 is neither composite nor prime

# Input:  n = 0
# Output: false
# Explanation: 0 is neither composite nor prime

def isPrime(n):
    if n <= 1:
        print("False")
        return

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            print("false")
            break
        
    print("true")

if __name__ == "__main__":
  n = int(input())
  isPrime(n)