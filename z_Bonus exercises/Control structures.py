"""Q- Imagine an alien was just shot down in a game. Create a variable called alien_color and
assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien’s color is green. If it is, print a message
that the player just earned 5 points.
•Write one version of this program that passes the if test and another that fails. (The
version that fails will have no output.)"""
#assign the color of the alien to the variable
alien_color = 'red'
#now check is the alien's color is red
if alien_color == 'red': 
    print("Congrats! you earned 5 points.") #if the condition is true this message will be printed

#FAILED VERSION WHICH WILL HAVE (NO OUTPUT).
#Assign the color to the variable 
alien_color = 'green'
#check if the alien's color is green 
if alien_color == 'yellow':
    print("Congrats, you earned 5 points.") #this won't print because the condition is false.
