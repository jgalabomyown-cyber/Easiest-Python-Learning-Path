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
print('\nFalsy and Truthy')
bool(0) # Falsy
bool('hello') # Truthy
bool(1) # Truthy
bool('') # Falsy

# for loops and the range() function
# syntax:
# for keyword
# variable name
# in keyword
# call to range() function w/ up  to 3 integers passed to it
# colon
# block of code / for clause(indented)
# Check Python_Exercises/fiveTimes.py
print('\n For Loop')
total = 0
for num in range(101):
    total = total + num

print(total)

# Equivalent while loop
# I added program in fiveTimes.py to show this loop

# Arguments to range()
# 2 Arguments
print('\n For Loop with Args')
for i in range (12, 16):
    print(i) # 12 13 14 15

# 3 Arguments
for i in range(0, 10, 2):
    print(i)

# looping down
for i in range(5, -1, -1):
    print(i)

# Importing Modules
# print(), input(), len(), type() - built-in functions
# set of modules = library
# import keyword
# name of module
# alias (i.e. as pd)
# check Python_Exercises/printRandom.py

# Ending a Program early with sys.exit()
# check Python_Exercises/exitExample.py

