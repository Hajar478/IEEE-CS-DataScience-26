import math

lmda = float(input())
x = int(input())
Po = ((lmda**x)*(1/(math.e)**lmda))/math.factorial(x)

print(f"{Po:.3f}")