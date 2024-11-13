"""### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input."""

#print what will the program do
print("This program will help in searching for a name in the list")

#list of the names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#ask what name are they looking for
find = input("What name are you looking for? ")

#now check if the name is in the list 
#this will let the user know both, if its available or not
if find in names:
    print("Yes, its available in the list!")
else:
    print("Sorry, its not in the list.")
