# Pair Cube Count

# Given n, count all ‘a’ and ‘b’ that satisfy the condition a^3 + b^3 = n. Where (a, b) and (b, a) are considered two different pairs

# Examples: 

# Input: n = 9
# Output: 2
# Explanation: 1^3 + 2^3 = 9 and 2^3 + 1^3 = 9


# Input: n = 28
# Output: 2
# Explanation: 1^3 + 3^3 = 28 and 3^3 + 1^3 = 28
import math

def countPairs(n):
    count = 0
    cubert = int(math.cbrt(n))
    
    for i in range(1, cubert+1):
        cube = i * i * i
        diff = n - cube
        
        cbrt_diff = int(math.cbrt(diff))
        
        if cbrt_diff * cbrt_diff * cbrt_diff == diff:
            count += 1
    
    return count

if __name__ == "__main__":
  n = 9
  print(countPairs(n))        