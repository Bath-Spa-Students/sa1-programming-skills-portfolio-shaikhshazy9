"""## Exercise 5: Days of the Month - 30 Marks

Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month."""

#This program will show the days in each month
print("Find out how many days are in a month")
month = int(input("Enter month number (1-12): ")) #get a month number from the user

#now check the month and print the days 
#it will check the month and print the number of days 
if month == 1:
    print("January has 31 days")
#if its month 1 (Jan) it will print January has 31 days. 
elif month == 2: 
    print("February has 28 days")
#same goes for all 
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
    print("Please enter a number between 1 and 12 only") #if you print numbers above 12 this will show up







