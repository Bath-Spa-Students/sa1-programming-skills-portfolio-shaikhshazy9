fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

cars = ["ls430", "ls460", "lx570"]
for x in cars:
  print(x)

#The break Statement
cars = ["ls430", "ls460", "lx570"]
for x in cars:
  print(x)
  if x == "ls460":
    break

#The range function
for x in range(8):
  print(x)

#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

#While loops
# With the while loop we can execute a set of statements as long as a condition is true.
# Print j as long as j is less than 10:

i = 1
while i < 10:
  print(i)
  i += 1  # i =i+1  

  count = 1
while count <= 5:
    print("Count is:", count)
    count += 1