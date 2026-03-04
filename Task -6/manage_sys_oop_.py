class Employee :

   def __init__(self , fname, lname, sal ):
      self.fname = fname
      self.lname = lname
      self.sal= sal

   def get_annual_salary(self):
      return self.sal*12
   
   def display_info(self):
      print(f"Employee Name : {self.fname} {self.lname}")
      print(f"Monthly Salary : {self.sal} ")
      print(f"Annual Salary : {self.get_annual_salary()}")
    

f_name ,l_name = list(input().split(" "))
monthlysalary =int(input())
emp1 =Employee(f_name,l_name,monthlysalary)

print(emp1.display_info())
