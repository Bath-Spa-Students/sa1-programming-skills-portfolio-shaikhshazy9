"""## Exercise 10: Is it even? - 35 Marks

Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function."""

#This function will check if number is even or odd.
def check_even_odd(number):
    #now if the number divides by 2 with no remainder using % it will be even
    if number % 2 == 0:
        return "It is even."
    else:
        return "Its odd."
    
#MAIN FUNCTION
def main():
    num = int(input("Enter a number: "))    #this asks for a number
    print(check_even_odd(num)) #this calls the check even odd function and prints result

main()

