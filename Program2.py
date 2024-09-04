# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.

name = input("Hey what's up? Tell me your name: ")
print("Oh hey " + name + "!")
print("It's great to meet you! You seem like a pretty cool person " + name + "!")


## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.

name = input("Hellooo! What's your name? -> ")
print("!" + name + "!" + name + "!")
print("I got something cool to show ya!")
print("0   0")
print("  |  ")
print("\___/\n")
print("It's a smiley face!")


## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630

print("Welcome, I will be asking you some questions to apply for this python competition.")
first_name = input("Hello, please tell me your first name: ")
last_name = input("Now tell me your last name: ")
street = input("What street do you live at? -> ")
city_postal = input("Now finally tell me your city and postal code: ")
print("Thank you for submitting your application!")
print("Here are your application details: ")
print("First name: " + first_name)
print("Last name: " + last_name)
print("Street address: " + street)
print("City and Postal Code: " + city_postal)
print("\n")
## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out

word1 = input("Tell me an ice cream flavor: ")
word2 = input("Tell me the name of a fruit: ")
word3 = input("Pick an icecream topping from (Sprinkles, ChocolateSyrup, Gummies, Jellybeans): ")
print("Here is your order of " + word1 + "Icecream-" + word2 + "-" + word3)
print("That's a cool order!\n")


## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.

print("Hello! I am going to write a story, but you get to choose the main character and the time it takes place!")
name = input("Give me the name of the protagonist: ")
year = input("Now give me a year (YYYY): ")
print("There once was an amazing individual named " + name + ".")
print("In " + year + ", " + name + " was going on a hike with friends.")
print("Suddenly, one of " + name + "'s friends Josh slipped off the edge!" )
print("Luckily, " + name + " grabbed Josh and brought him up to safety!")
