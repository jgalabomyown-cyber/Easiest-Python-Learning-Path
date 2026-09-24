# 1. While Loops
# while condition: 
    #do something

# This code below is causing infinite bug
# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input('>')
# print('Thank you!')

# Break Statement
# while True:
#     print('Please type your name.')
#     name = input('>')
#     if name == 'your name':
#         break
# print('Thank you!')

# Continue statements
# Program execution immediately jumps back to the start of 
# the loop and reevaluates the loop conditions

# For the project of this topic see Python_Exercises/swordfish.py

# Truthy and Falsy
0, 0.0, '' # Falsy Values

name = ''
while not name:
    print('Enter your name: ')
    name = input('>')
print('How many guest will you have?')
num_of_guests = int(input('>'))

if num_of_guests:
    print('Be sure to have enough room for all your guests.')
print('Done')

# Bool Function - to identify if certain values are
# truthy or falsy
bool(0) # Falsy
bool('hello') # Truthy
bool(1) # Truthy
bool('') # Falsy

