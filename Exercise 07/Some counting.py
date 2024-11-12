"""## Exercise 7: Some Counting - 20 Marks

Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*"""

#Program which counts numbers in different ways
#First loop: count from 0 to 50 in increments of 1

print("Counting up from 0 to 50:")
for number in range(0,51):  #note we use 51 as the end number because range excludes the end number
    print(number)

#add blank line between loops it makes the output reading easier
print()    

#Second loop: count from 50 to 0 (down)
#the -1 is used for counting backwards
print("Counting down from 50 to 0:")
for number in range(50, -1, -1): #we use -1 as the end number because we want to include 0
    print(number)
print()    

#Third loop: count from 30 to 50
#this shows we can count up from any number
print("Counting from 30 to 50:")
for number in range(30, 51):
    print (number)
print()    

#Fourth loop: count down 50 to 10 by 2s
#-2 means count down by 2s
print("Counting down 50 to 10 by 2s")
for number in range(50, 9, -2):  
    print(number)
print()    

#Fifth loop: Count up from 100 to 200 by 5s
print("Count up from 100 to 200 by 5s")
for number in range(100, 201, 5): #201 is used to show 200 in the output
    print(number)