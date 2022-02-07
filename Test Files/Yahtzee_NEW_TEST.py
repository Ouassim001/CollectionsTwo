import time
import random

rolls = []
{1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
while True:
    def dice_roll():

        again = "try again"
        rolls = []
        print("Welcome to 5 Dice!")
        input("Press ENTER to roll")
        for x in range(5):
            rolls.append(random.randint(1,6))
            rolls.sort()
            print(rolls)
        counts = []
        for i in range(5):
            counts.append(rolls.count(i + 1))
            counts.clear()
            
            if rolls[0] == 1 and rolls[0] == 1 and rolls[0] == 1:
                print("Three of a kind")

            if rolls[1] == 2 and rolls[1] == 2 and rolls[1] == 2 and rolls[1] == 2:
                print("Four of a kind")
            

        

            # if rolls[0] in rolls:
            #     print("three of a kind!")
            #     try_again()
            # if rolls[1] in rolls:
            #     print("four of a kind!")
            #     try_again()
            # if rolls[2] and  rolls:
            #     print("five of a kind!")
            #     try_again()
            # if rolls[0] in rolls:
            #     try_again()
        
    def try_again():
        choice = input("Wil je nog een keer spelen? Y/N: ")
        if choice == "Y" or choice == "y":
            dice_roll()
        if choice == "N" or choice == "n":
            print("ok")
                    
        else:
            print("TYPE Y of N")

    

    dice_roll()
    try_again()
