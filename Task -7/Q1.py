import math

line_nums= list(map(float,input().split(" ")))
p_boy = line_nums[0]/(line_nums[0]+line_nums[1])
q = 1 - p_boy
n=6

result = 0
for x in range(3,7):
    result += math.comb(n,x)* (p_boy**x)* (q**(n-x))

print(f"{result:.3f}")    