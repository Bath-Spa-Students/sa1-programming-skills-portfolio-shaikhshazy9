# Void function 
def print_message():
    print("Hello everyone")
# Calling function 
print_message()

# Local variable 
def print_message():
    message ="Hello everyone"  # Local variable 
    print(message)
# Calling function 
print_message()


#Diffenrent functions have same local variables name 

def print_message():
  message ="hi"
  print(message)
  
def print_message_2():
  message ="hello"
  print(message)

print_message()
print_message_2()