# Import random module
import random

# Define character pool
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'
SYMBOLS = '!#$%&()*+,-./:;<=>?@[]^_`{|}~'

# Define password variable
password = ''

# Functions
# Ask user for password length
def askLength():
	password_length = int(input('How long do you want your password to be? (6-20 characters) \n'))

	# Determine is input is valid
	if password_length >= 6 and password_length <= 20:
		return password_length
	else:
		print('Inavlid input, go to school loser')
		return askLength()

# Add a random lowercase letter to the password variable
def addLowerLetter():
	global LETTERS
	global password

	password += random.choice(LETTERS)


# Add a random uppercase letter to the password variable
def addUpperLetter():
	global LETTERS
	global password

	password += random.choice(LETTERS).upper()


# Add a random number to the password variable
def addNumber():
	global NUMBERS
	global password

	password += random.choice(NUMBERS)

# Add a random symbol to the password variable
def addSymbol():
	global SYMBOLS
	global password

	password += random.choice(SYMBOLS)

# Create a list with previous functions
password_functions = [addLowerLetter, addUpperLetter, addNumber, addSymbol]

# Adds a random character type for length of the password
def main():

	global password
	
	password_length = askLength()

	for i in range(password_length):
		random.choice(password_functions)()

	return password

print(main())