# Subtract 1 without arithmetic operators
# Write a program to subtract one from a given number. The use of operators like ‘+’, ‘-‘, ‘*’, ‘/’, ‘++’, ‘–‘ …etc are not allowed. 

# Examples: 

# Input:  12
# Output: 11


# Input:  6
# Output: 5

def subtractOne(x):
    m = 1
    
    while((x & m) == False):
        x = x ^ m
        m = m << 1
        
    x = x ^ m
    return x

print(subtractOne(12))