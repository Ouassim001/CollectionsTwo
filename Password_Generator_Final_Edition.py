import random
letters = "abcdefghijklmnopqrstuvwxyz"
nummers = "0123456789"
symbols = "!@#$%^&*()_-=[]?/{|}"
password = ""


def main():
    global password
    password_lengte = vraaglengte()
    
    for i in range(password_lengte):
        random.choice(password_functions)()
        return password


def vraaglengte():
    lengte = int(input("hoelang moet jou wachtwoord zijn? (tussen 4 en 24 karakters) \n"))
    if lengte >= 4 and lengte <= 24:
        return lengte
    else:
        print("probeer opnieuw. type een nummer tussen 4 en 24")
        return vraaglengte()
        
def addLowerLetter():
    global letters
    global password

    password += random.choice(letters)     

def addUpperLetter():
    global letters
    global password

    password += random.choice(letters).upper()

def addNummer():
    global nummers
    global password

    password += random.choice(nummers)

def addSymbols():
    global symbols
    global password

    password += random.choice(symbols)


password_functions = [addLowerLetter, addUpperLetter, addNummer, addSymbols]
random.choice(password_functions)()

def main():

	global password
	
	password_lengte = vraaglengte()

	for i in range(password_lengte):
		random.choice(password_functions)()

	return password


print(main())