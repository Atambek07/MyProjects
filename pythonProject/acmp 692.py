def is_binary(n): 
    if n <= 0: 
    	return False 
    while n % 2 == 0: 
        n //= 2 
    return n == 1

N = int(input()) 
if is_binary(N): 
    print("YES") 
else:
    print("NO")