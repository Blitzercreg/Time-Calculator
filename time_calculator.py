import sys

# Introduction to the application
intro = "Welcome to the time calculator!"
instructions = "Please enter 'q' at anytime to quit"
banner = '-' * len(intro)
print(banner)
print(intro)
print(banner)
print(instructions + '\n')

# Start application loop
while True:

	# First time entry
	while True:
		time_0 = input("Please enter the time you started: ")
		if time_0 == 'q':
			sys.exit()
					
		try:
			time_0 = float(time_0)
			break
		except ValueError:
			print('Thats not a number!')

	am_pm_0 = input('am or pm: ')
	if am_pm_0 == 'q':
		sys.exit()
	
	am_pm_0 = am_pm_0.strip()
	am_pm_0 = am_pm_0.lower()

	while (am_pm_0 != 'am') and (am_pm_0 != 'pm'):
		print("That is not an acceptable format.")
		am_pm_0 = input('am or pm: ')
		if am_pm_0 == 'q':
			sys.exit()

		am_pm_0 = am_pm_0.strip()
		am_pm_0 = am_pm_0.lower()

	if am_pm_0 == "pm":
		time_0 = time_0 + 12

	# Second time entry
	while True:
		time_1 = input("Please enter the time you ended: ")
		if time_1 == 'q':
			sys.exit()

		try:
			time_1 = float(time_1)
			break
		except ValueError:
			print('Thats not a number!')

	am_pm_1 = input('am or pm: ')
	if am_pm_1 == 'q':
		sys.exit()
	
	am_pm_1 = am_pm_1.strip()
	am_pm_1 = am_pm_1.lower()

	while (am_pm_1 != 'am') and (am_pm_1 != 'pm'):
		print("That is not an acceptable format.")
		am_pm_1 = input('am or pm: ')
		if am_pm_1 == 'q':
			sys.exit()
	
		am_pm_1 = am_pm_1.strip()
		am_pm_1 = am_pm_1.lower()

	if am_pm_1 == "pm":
		time_1 = time_1 + 12

	# Time calculation
	hours = time_1 - time_0
	if hours < 0:
		hours = hours * -1

	print(f"Your total hours: {hours}")

	# Restart application argument
	answer = input("Would you like to enter more time? (y/n):")
	if answer == 'n':
		break