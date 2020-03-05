# -------------------------------------- 1- Comments in Python --------------------------------------:
#This is a single line comment

'''
This is a
multi line comment using 3 single quotations
'''

"""
This is a
multi line comment using 3 double quotations
"""

# -------------------------------------- 2- Declaring a variable --------------------------------------:
#
# Rules:
# 1- Start with _ or letters, cannot start with a number
# 2- Accepted alpha-numeric are: (A -> Z) (a -> z) (0 -> 9) (_). Dash(-) is not accepted
# 3- variables are case sensitive: name != Name

#Legal naming
_myid = 20
_my_id = 20
my_id = 20
MyId = 20
myId = 20
myid1 = 20

#Illegal naming
#my-id = 20
#1myId = 20
#my id = 20

# -------------------------------------- 3- Variable Datatype --------------------------------------:
#In python datatype decleration is required
varTest = 1 #this is an Integer
varTest = "I am a string now :)" #varTest took a new value and is a String

# -------------------------------------- 4- Outputting variables value  --------------------------------------:
#Use print() function to display the data of variables. Put the name of the varaible inside the parentheses ()
hello = "Hello World"
print(hello) # -> prints "Hello World"

# Printing a new line
print("One\nTwo\nThree") #Outputs One,Two and Three each in a new line

# Concatenating variables and strings
print("1: " + hello + "!") #Result -> "1: Hello World!"

# -------------------------------------- 5- Declaring Multiple Variables  --------------------------------------:
a = b = c = "We are all the same "
print(a + "\n" + b + "\n" + c) #







