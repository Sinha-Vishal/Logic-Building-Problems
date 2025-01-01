# Problem: Find the number closest to n and divisible by m
# Given two integers n and m (m != 0). Find the number closest to n and divisible by m.
# If there is more than one such number, then output the one having maximum absolute value.

# Examples: 

# Input: n = 13, m = 4
# Output: 12
# Explanation: 12 is the closest to 13, divisible by 4.


# Input: n = -15, m = 6
# Output: -18
# Explanation: Both -12 and -18 are closest to -15, but-18 has the maximum absolute value.

def closest_number(n, m):
    closest = 0
    min_difference = float('inf')
    
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n - i)
            
            if difference < min_difference or (difference == min_difference and abs(i) > abs(closest)):
                closest = i
                min_difference = difference
    return closest

if __name__ == "__main__":
    n = int(input())
    while True:
        m = int(input("Enter the value of m (should not be 0): "))
        if m != 0:
            break
        print("m cannot be 0. Please re-enter.")

    print("Closest number:", closest_number(n, m))