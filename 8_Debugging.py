# Methodology
# 1. Raising Exception
# a. raise keywork
# b. call to the Exception() function
# c. helpful message string to the Exception() function

raise Exception('This is an error message')
# check /Python_Exercises/8_boxPrint.py

# 2. Assertions
#  => sanity check to make sure the code isn't doing the obvious mistake
#  a. assert keyword
#  b. a condition(that is, an expression(evaluates True or False))
#  c. a comma
#  d. a string to display the condition is False
#  => are for programmer errors and not the users

# 3. Logging
#  => using the print() function to debug the code e.g.
# a. The logging Module import logging

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# open /Python_Exercises/8_factorialLog.py

# 4. Logfiles
#  => storing the log messages into text file
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
format=' %(asctime)s - %(levelname)s - %(message)s')

# Logging Levels
# DEBUG >> logging.debug() >> lowest level, for small details, to diagnose problem
# INFO  >> logging.info()  >> to record info for general events of the program, to confirm the program is working
# WARNING >> logging.warning() >> to indicate a potential problem that doesn't prevent the program from working but might do so in the future
# ERROR >> logging.error() >> to record an error that caused the program to fail on doing something
# CRITICAL >> logging.critical() >> highest level, used to indicate fatal error that has caused, about to cause, the program to stop running entirely

# Disabled Loggin
# disables log messages

