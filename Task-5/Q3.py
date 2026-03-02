#nth person or last one at the end has one seat so it's either his own or not so p=0.5 only for the last person 
n = int(input())
def nthperson(n):
    if n == 1:
        return 1
    else:
        return 0.5 
    
p=nthperson(n)
print(p)



