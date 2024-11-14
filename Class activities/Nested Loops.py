adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#Nested Loops  -- A loop withon a loop
x= [1,2,3]
y=[4,5,6]
for i in x:
    for j in y:
        print (i,j)
# Another Example 

for i in range (2):   # 0,1,
    
      for j in range(3) :  #0,1,2
             print("outer loop" ,i , "Inner Loop" , j )