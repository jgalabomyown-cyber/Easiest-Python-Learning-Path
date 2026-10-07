def collatz(number):
	if number % 2 == 0:
		result = number // 2

	else:
		result = 3 * number + 1

	print(result, end=' ')
	return result

# --- Code runs start here ----
print('Enter a number: ')
while True:
	try:
		user_number = int(input('> '))
		break
		# Keep calling the function until it returns 1

	except ValueError:
		print('Please enter a valid integer.')
		print()

while user_number != 1:
	user_number = collatz(user_number)

print()
