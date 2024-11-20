"""Q- Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza."""
#start with a loop 
while True: 
    topping = input("Enter topping or stop: ") #asks about the toppings
    if topping == 'stop':
        break #exit loop
    #this is the message for the topping
    print("Adding", topping, "to your pizza!")