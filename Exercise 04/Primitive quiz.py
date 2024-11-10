"""Exercise 4: Primitive Quiz - 30 Marks
In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.
Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong.
Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question."""

#This program asks a question about France's capital and checks the answer
print("Welcome to the capital city quiz") #Print an welcome message 

#ask the question and store the answer of the user 
answer = input("What is the capital of France? ")

#check if answer is correct 
if answer == "Paris":
    #if answer is correct print an correct message 
    print("Correct! The answer is Paris")
else: print("No that's wrong, The capital of France is Paris.") #if answer is wrong it will print this messsage


