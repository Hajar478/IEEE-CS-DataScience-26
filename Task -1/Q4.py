x = int(input('Num1 :'))
y = int(input('Num2 :'))
opr = input('Operator :')

result = eval(f"{x}{opr}{y}") # eval: it makes a string equation to be calculatable
print(result)


#---------------------------------
#or
"""
if opr == "+":
    result = x+y
    print(round(result),2) 
elif opr == "-":
    result = x-y
    print(round(result),2)
elif opr == "*":
    result = x*y
    print(round(result),2)
elif opr == "/":
    result = x/y
    print(round(result),2)
else: 
    print(f"{opr} is not valid")
    """