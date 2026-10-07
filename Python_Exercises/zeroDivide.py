def divided_by(number):
	try:
		return 42 / number

	except:
		print('Error: Invalid Argument')

print(divided_by(2))
print(divided_by(12))
print(divided_by(0)) #ZeroDivisionError if no Exception Handling
print(divided_by(7))

