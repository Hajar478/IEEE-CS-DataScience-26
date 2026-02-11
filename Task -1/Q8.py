import math

x1 ,y1 = map(float,(input("P1 : " ).split()))
x2 ,y2 = map(float,(input("P2 : " ).split()))

d = float(math.sqrt(pow((x2-x1),2)+pow((y2-y1),2)))
print(d)