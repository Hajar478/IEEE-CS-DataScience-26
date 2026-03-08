import math

line_nums= list(map(int,input().split(" ")))
n = line_nums[1]
p = line_nums[0]/100
q = 1 - p


P2 = 0
for x in range(3):  #at most 2
    P2 += math.comb(n,x)* (p**x)* (q**(n-x))

print(f"{P2:.3f}")   

P1 = 0
for x in range(2,n+1):  #at lesat 2
    P1 += math.comb(n,x)* (p**x)* (q**(n-x))

print(f"{P1:.3f}")   
