import random
Three_Of_A_Kind = []
Four_Of_A_Kind = []
Small_Straight = []
Large_Straight = []
Full_House = []

def dice():
    for rolls in range(5):
        t = print(random.randint(1, 6))
        rolls = t
        
dice = dice()

def keep(dice):
    YofN = input("wil je nummers bijhouden  ja/nee?\n").lower
    if YofN == "nee":
        print("ok")
    elif YofN == "ja":
        num1()




def num1(dice):
    much = int(input("Hoeveel nummers wil je bijhouden"))
    for y in range(much):
        input("Wat is het volgende nummer?\n")




def num2(dice):
    
