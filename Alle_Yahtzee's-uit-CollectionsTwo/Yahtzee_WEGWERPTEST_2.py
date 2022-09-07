scores = [5,6,31,4,0]

titles = ["small straight", "large straight", "three of a kind", "four of a kind", "Full house"]

for s in range(5):
    print()
    print(" {:20}  :  |_-_|".format(titles[s]) + "{:2} |_-_|".format(scores[s]))  


import random
def dice_roll():
    number_of_dice = 5
    again = "try again"
    rolls = []
    print("Welcome to 5 Dice!")
    input("Press ENTER to roll")
    for x in range(number_of_dice):
        rolls.append(random.randint(1,6))
        rolls.sort()
        print(rolls)
        if rolls[0] == rolls[1]:
            print("You rolled a three of a kind!")
            print(again)
        if rolls[1] == rolls[2]:
            print("You rolled a four of a kind!")
            print(again)
        if rolls[2] == rolls[3]:
            print("You rolled a five of a kind!")
            print(again)
        if rolls[3] == rolls[4]:
            print(again)
dice_roll()


