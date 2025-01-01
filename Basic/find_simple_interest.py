# Problem: Program to find simple interest
# Given Principal p, Rate r and Time t, the task is to calculate Simple Interest.

# Examples :

# Input: p = 10000, r = 5, t = 5 
# Output:2500 
# Explanation: We need to find simple interest on  Rs. 10,000 at the rate of 5% for 5  units of time.  


# Input: p = 3000, r = 7, t = 1 
# Output:210

def simpleInterest(p, r, t):
    return (p * r * t) / 100

if __name__ == "__main__":
    p = float(input())
    r = float(input())
    t = float(input())
    print(simpleInterest(p, r, t))