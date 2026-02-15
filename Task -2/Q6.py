import random
import string 

chars = string.ascii_uppercase+string.ascii_lowercase+string.digits
password = ""
for i in range(8):
   password += random.choice(chars)
print(password)

