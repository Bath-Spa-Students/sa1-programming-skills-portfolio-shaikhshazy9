"""### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly."""

#This program will show days in each month with leap year check
print("Find out how many days are in a month")
month = int(input("Enter month number (1-12): ")) #get any month number from the user

#now check each month
if month == 1:
    print("January has 31 days")

elif month == 2: 
    leap = input("Is it a leap year? (yes/no): ") #here it will ask about leap year 
    if leap == "yes":
        print("February has 29 days") #if ans is yes it will print this
    else:
        print("February has 28 days") #if no then it will print as 28 

elif month == 3: 
    print("March has 31 days")

elif month == 4:
    print("April has 30 days")

elif month == 5: 
    print("May has 31 days")

elif month == 6:
    print("June has 30 days")

elif month == 7: 
    print("July has 31 days")

elif month == 8: 
    print("August has 31 days")

elif month == 9:
    print("September has 30 days")

elif month == 10:
    print("October has 31 days")

elif month == 11: 
    print("November has 30 days")

elif month == 12: 
    print("December has 31 days")

else:
    print("Please enter a number between 1 and 12 only")