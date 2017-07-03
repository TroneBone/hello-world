import string
import random
password = ""
for i in range(12):
    password += random.choice(string.printable)
print(password)