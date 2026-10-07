# Functions
# - mini program within a program
def hello():
    # Prints three greetings
    print('Good morning!')
    print('Good afternoon!')
    print('Good evening!')

hello()

# Arguments and Parameters
print('\n--------- Arguments and Parameters-----------')
def say_hello_to(name):
    # Print three greetings to the names
    print('Good morning, ' + name + '!')
    print('Good afternoon, ' + name + '!')
    print('Good evening, ' + name + '!')
    print(name) # works

say_hello_to('Alice') # calls
say_hello_to('Bob')  
# print(name) # will not work because of the variable-scope

# Return Values and Return Statements
print('\n--------- Return Values and Return Statements-----------')
print('check Python_Exercises/magic8ball.py')

# The None Value
# Absence of Value
# The only Value that is NoneType data type (null, undefinced, nil)
