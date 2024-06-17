#random password generator
import random

print("\nRANDOM PASSWORD GENERATOR\n")
pwd_count=int(input("Number of password needed:"))
pwd_chars=int(input("Number of characters:"))

#possible characters for password
password="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&"

print("\nThe Passwords are:-")
print("-----------------------")

#loop to iterate number of passwords
for i in range(pwd_count):
    pwd=""
    #loop to iterate number of characters
    for x in range(pwd_chars):
        pwd=pwd+random.choice(password)

    print("Password#"+str(i+1)+": "+pwd)    

print("-----------------------")
print("THANK YOU :) \n")
