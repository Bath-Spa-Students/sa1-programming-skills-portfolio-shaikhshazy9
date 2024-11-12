"""### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
"""
#This program will check password 
#But it will only have 5 attempts
print("Enter the password")
print("You only have 5 attempts")
attempts = 5 

#Keep asking until the attempts are left
while attempts > 0:
    password = input("Password: ")
    if password == "12345":
        print("Correct password!")
        break
    attempts = attempts - 1
    print("Wrong!")   #if the password is wrong print wrong and it will take 1 attempt each time you get wrong
    print("Attempts left:", attempts)

    if attempts == 0: #check if all attempts are used
        print("Alerting the authorities!")   #if all used show up this message