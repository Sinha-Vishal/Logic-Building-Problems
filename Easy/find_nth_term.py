# Find n-th term of series 1, 3, 6, 10, 15, 21…
# Given a number n, find the n-th term in the series 1, 3, 6, 10, 15, 21…

# Examples: 

# Input : 3
# Output : 6

# Input : 4
# Output : 10 

def term(n):
    return n * (n+1) / 2

print(term(4))
    