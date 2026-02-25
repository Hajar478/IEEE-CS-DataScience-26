import math

def get_numbers():
    attempts=3
    while attempts>0:
        try:
            befor_list=input()
            if not befor_list.strip():
                raise ValueError("Empty input, enter values")
            
            if ',' in befor_list or ';'in befor_list:
                raise ValueError("invalide input, only use space separator") 
            
            after_list=list(map(int,befor_list.split()))
            return after_list
        except ValueError as v:
            attempts -=1
            print("Error : ",v)
            print(f'You have {attempts} left')
  
records = get_numbers()#هستخدم الليست المترتبه ف كل حاجه لكن دي هستخدمها عشان اطلع الترتيب بس 

def sort_r(records):#bubble sortعشان استفيد من مذاكره الجورزم 
   n=len(records)

   for i in range(n):
      for j in range(0,n-i-1):
         if records[j]>records[j+1]:
            temp=records[j]
            records[j]=records[j+1]
            records[j+1]=temp

   return records  

numbers= sort_r(records)   
n=len(numbers)
def sum_r(numbers):
   #n=len(numbers)
   total=0
   for i in range(n):
      total +=numbers[i]

   return total

sum_=sum_r(numbers)  

def find_max(numbers):
   max_val=numbers[n-1]
   return max_val

max_=find_max(numbers)
           
def find_min(numbers):
    min_val=numbers[0]
    return min_val

min_=find_min(numbers)    

def find_mean(numbers):
   mean_val=sum_/n
   return mean_val

mean_=find_mean(numbers)

def find_mode(numbers):
   freq={}
   for j in numbers:
      if j in freq:
         freq[j] +=1
      else:
         freq[j] =1
   mode_l=[j for j in freq if freq[j]>1]
   return mode_l

mode_=find_mode(numbers)            

def find_median(numbers):
   n_all=len(numbers)
   if n_all%2 == 0 : #even
      median_=(numbers[(n_all//2)-1] + numbers[n_all//2]) / 2
   else:#ood
      median_=numbers[(n_all//2)]
   return median_

median_=find_median(numbers)    

def find_range(numbers):
   range_val=max_- min_
   return range_val

range_= find_range(numbers)

def find_variance(numbers):
   dev = 0
   for x in range(n):
      dev += (numbers[x]-mean_)**2
   var = dev/n
   return var

var_= find_variance(numbers)   

def find_STD(numbers):
   STD =math.sqrt(var_)
   return STD

std_= find_STD(numbers)

def find_Quartiles(numbers):#Q1 Q2 Q3
   q2= median_
   mid = n//2
   if n%2 == 0:#big list is even
      half1 = numbers[:n//2]
      half2 = numbers[n//2:]
   else: #big list is odd
      half1 = numbers[:mid]
      half2 = numbers[mid+1:]
       
    
   q1 = find_median(half1)
   q3 = find_median(half2)
   return q1 ,q2 ,q3  

Q1 ,Q2 ,Q3 = find_Quartiles(numbers)

def find_IQR(numbers):
   iqr= Q3 - Q1
   return iqr

iqr_ =find_IQR(numbers)

print(f'Min Heart Rate: {min_}')
print(f'Max Heart Rate: {max_}')
print(f'Mean Heart Rate: {mean_:.2f}')
print(f'Mode : {mode_}')
print(f'Median : {median_:.2f}')
print(f'Range: {range_}')
print(f'Variance: {var_:.2f}')
print(f'Standard Deviation: {std_:.2f}')
print(f'Quartiles: {Q1} {Q2} {Q3}')
print(f'Interquartile Range (IQR) : {iqr_}')