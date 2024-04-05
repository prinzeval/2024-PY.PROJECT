import string
import random

limit = int(input("ENTER ANY LIMIT : "))
password = ""
char = string.ascii_letters
char += string.digits
char += (".!@#$%^&*90-+"":';") 

for i in range (limit):
    cb = random.choice(char)
    password += cb 

print(password)




