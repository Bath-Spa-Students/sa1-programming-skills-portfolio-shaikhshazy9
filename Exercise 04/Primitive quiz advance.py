"""Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question. """

#This program asks questions about capitals of 10 European countries
#Program will accept answers in any capitilization Uppercase or Lowercase
print("Welcome to the European capitals quiz") #print a welcome message 

#Question 1
ans = input("What is the capital of France? ")
if ans.lower() == "paris": 
    print("Correct!")
else:
    print("No, its Paris")

#Question 2 
ans = input("What is the capital of Germany? ")
if ans.lower() == "berlin":
   print("Correct!")
else: 
    print("No, its Berlin")

#Question 3
ans = input("What is the Capital of Italy?")
if ans.lower() == "rome": 
    print("Correct!")
else:
    print("No, its Rome")

#Question 4 
ans = input("What is the capital of Spain?")
if ans.lower() == "madrid":
    print("Correct!")
else:
    print("No, its Madrid")    

#Question 5
ans = input("What is the capital of Portugal?")
if ans.lower() == "lisbon":
   print("Correct!")
else: 
    print("No, its Lisbon")

#Question 6 
ans = input("What is the capital of United Kingdom?")
if ans.lower() == "london":
    print("Correct!")
else:
    print("No, its London")

#Question 7 
ans = input("What is the capital of Ireland?")
if ans.lower() == "dublin":
    print("Correct!")
else:
    print("No, its Dublin")     

#Question 8 
ans = input("What is the capital of Sweden? ")
if ans.lower() == "stockholm":
    print("Correct!")
else: 
    print("No, its Stockholm")

#Question 9
ans = input("What is the capital of Greece? ")
if ans.lower() == "athens":
    print("Correct!")
else:
    print("No, its Athens")    

#Question 10 
ans = input("What is the capital of Netherlands? ")
if ans.lower() == "amsterdam":
    print("Correct! ")
else:
    print("No, its Amsterdam")
    
#Quiz finished
print("Quiz completed! ")
print("Thanks for playing")


        
       

