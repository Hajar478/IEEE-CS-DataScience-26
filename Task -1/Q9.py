num = int(input())
num_len = len(str(num))

temp=num
sum=0
while temp > 0:
    digit = temp % 10
    sum += digit ** num_len
    temp = temp // 10       #loop end 

if sum == num:
    print(f"{num} is an Armstrong number ")
else:
    print(f"{num} isn't an Armstrong number ")