"""## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered."""

#This is a password checking program
print("Enter your password!")
while True:  #use while true loop to keep asking until you enter the correct one
    password = input("Enter password: ")

    #check if the password matches
    if password == "12345":
        print("Correct")
        break
    print("Wrong please try again")




