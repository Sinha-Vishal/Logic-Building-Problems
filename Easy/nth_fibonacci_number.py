# Nth Fibonacci Number
# Given a positive integer n, the task is to find the nth Fibonacci number.

# The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21

def find_nth_fibonacci(n):
    
    if n <= 1:
        return n
    
    fibo = [0, 1]
    
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
        
    return fibo[n]

print(find_nth_fibonacci(2))
        
    