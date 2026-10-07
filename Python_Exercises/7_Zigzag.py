import time, sys

indent = 0
indent_increasing = True

try:
	while True: # Main program loop
		print(' ' * indent, end = '')
		print('********')
		time.sleep(0.1) # Pause for 1/10 of a second

		if indent_increasing:
			# Increase the number of spaces
			indent = indent + 1
			if indent == 20:
				# Change direction
				indent_increasing = False

		else:
			# Decreasee the number of spaces
			indent = indent - 1
			if indent == 0:
				# Change direction
				indent_increasing = True

except KeyboardInterrupt:
	sys.exit()
