def countSetBits( n):
     
    # base case
    if (n == 0):
        return 0
 
    else:
 
        # if last bit set add 1 else add 0
        return (n & 1) + countSetBits(n >> 1)
         

n = int(input())
print( countSetBits(n)) 