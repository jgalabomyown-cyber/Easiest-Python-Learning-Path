import time, sys

try:
	while True:
		# Draw lines in increasing length
		for i in range(1, 9):
			print('-' * (i * i))
			time.sleep(0.1)

		# Draw lines in decreasing length
		for i in range(7, 1, -1):
			print('-' * (i * i))
			time.sleep(0.1)

except KeyboardInterrupt:
	sys.exit()
