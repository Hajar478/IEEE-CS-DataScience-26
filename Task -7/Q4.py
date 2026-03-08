import math 
line1 = list(map(int,input().split(" ")))
mu = line1[0] 
segma = line1[1]
x = float(input())
line2 = list(map(int,input().split(" ")))
xa = line2[0]
xb = line2[1]

p_less = 0.5*(1+math.erf((x-mu)/(segma*math.sqrt(2))))

p_between = 0.5*(1+math.erf((xb-mu)/(segma*math.sqrt(2))))-0.5*(1+math.erf((xa-mu)/(segma*math.sqrt(2))))

print(f"{p_less:.3f}")
print(f"{p_between:.3f}")
