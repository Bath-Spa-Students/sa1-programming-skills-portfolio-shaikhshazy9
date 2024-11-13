"""## Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam"."""
#List of names
names= ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#print the list to check whats in it
print("The list of names:", names)
#check if Sam is in the list
if "Sam" in names:
    print("Found Sam!")
else:
    print("Can't find Sam in the list")
