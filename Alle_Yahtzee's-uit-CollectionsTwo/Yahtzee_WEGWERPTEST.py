# import random
# Three_Of_A_Kind = []
# Four_Of_A_Kind = []
# Small_Straight = []
# Large_Straight = []
# Full_House = []
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def dice():
#     print("Turn 1")
#     for rolls in range(5):
#         t = print(random.randint(1, 6))
#         rolls = t
        
# dice = dice()


# def keep(dice):
#     num1  = input("type je cijfer die je wilt achterhouden, Zoniet hit ENTER\n").lower
#     if num1 in numbers:
#         ThreeOfKind()
#     else:
#         ThreeOfKind
#         return dice

# keep(dice)


# def ThreeOfKind(dice):
#     threeKind = []






while True:
  def mainMenu():
    while True:
      inputMenu = print("Welcome bij Yahtzee!\n")
      print("\n")
      break


  def of_kind(dice):
      ofAKind = 1
      for x in range(5):
          current=x
          count=1
          while count != -1:
              if current + 1 < 5:
                  if dice[current + 1] == dice[x]:
                      current = current + 1
                      count = count + 1
                      if count > ofAKind:
                          ofAKind = count
                  else:
                      count = -1
              else:
                  count = -1

      if ofAKind == 5:
          print("Je hebt een YAHTZEE gescoord!: 50 punten.\n\n")
          return 50

      elif ofAKind == 4 or ofAKind == 3:
          total = 0
          for index in range(5):
              total = total + int(dice[index])
          if ofAKind == 4:
              total = total + 10
              print("Je hebt een Four of a Kind gescoord!: " + str(total) + " punten.\n\n")
              return total
          else:
              noDuplicates = []
              for index in range(5):
                  if dice[index] not in noDuplicates:
                      noDuplicates.append(dice[index])
              if len(noDuplicates) == 2:
                  print("Je hebt Full House gescoord!: 25 punten.\n\n")
                  return 25
              else:
                  total=total+5
                  print("Je hebt een Three of a Kind gescoord!: " + str(total) + " punten.\n\n")
                  return total
      else:
          return 0
  prob = of_kind()
  print(prob)

  mainMenu()
  of_kind()














# hieronder begint yahtzee FULL
import random

#test pairs
def of_kind(dice):
    Three_Of_A_Kind = []
    Four_Of_A_Kind = []
    Small_Straight = []
    Large_Straight = []
    Full_House = []
    of_a_kind = 1
    for x in range(5):
        current = x
        count = 1
        while count != -1:
            if current + 1 < 5:
                if dice[current + 1] == dice[x]:
                    current = current + 1
                    count = count + 1
                    if count > of_a_kind:
                        of_a_kind = count
                else:
                    count = -1
            else:
                count = -1

    if of_a_kind == 5:
        print("Five of a Kind: 50 points.")
        return 50
    
    elif of_a_kind == 4 or of_a_kind == 3:
        total = 0
        for index in range(5):
            total = total + int(dice[index])
        if of_a_kind == 4:
            total = total + 10
            print("Four of a Kind: " + str(total) + " points.")
            return total
        else:
            no_duplicates = []
            for index in range(5):
                if dice[index] not in no_duplicates:
                    no_duplicates.append(dice[index])
            if len(no_duplicates) == 2:
                print("Full House: 25 points.")
                return 25
            else:
                total = total + 5
                print("Three of a Kind: " + str(total) + " points.")
                return total
    else:
        return 0

def straight(dice):
    straight = 1
    for index in range(len(dice)):
        current = index
        count = 1
        while(current != -1):
            if current + 1 < len(dice):
                if int(dice[current + 1]) - int(dice[current]) == 1:
                    current = current + 1
                    count = count + 1
                elif int(dice[current + 1]) == int(dice[current]):
                    current = current + 1
                else:
                    current = -1
            else:
                current = -1
            if count > straight:
                straight = count
    if straight == 4:
        print("Small Straight: 30 points.")
        return 30
    elif straight ==5:
        print("Large Straight: 40 points.")
        return 40
    else:
        return 0

def patterns(dice):
    score = of_kind(dice)
    if score == 0:
        score = straight(dice)
    if score == 0:
        print("No Pattern: 0 points.")
    return score

    
def main():
    total_score = 0
    for x in range(1,6):
        print("Turn " + str(x) + "!")
        dice = []
        for x in range(5):
            dice.append(random.randint(1,6))
        print("Roll 1: ", end ="")
        for x in range(len(dice)):
            if x < len(dice) - 1:
                print(dice[x], end =" ")
            else:
                print(dice[x])
            
        keep = input("Which numbers would you like to keep? ")
        keep = keep.split(',')
        print("Roll 2: ", end ="")
        for x in range(5):
            if str(x + 1) not in keep:
                dice[x] = random.randint(1,6)
            if x < len(dice) - 1:
                print(dice[x], end =" ")
            else:
                print(dice[x])
        dice.sort()
        score = patterns(dice)
        total_score = total_score + score
      
    scores = [score, ]

    titles = ["small straight", "large staright", "three of a kind", "four of a kind", "Full house"]

    for s in range(5):
        print()
        print(" {:20}  :  |_-_|".format(titles[s]) + "{:2} |_-_|".format(scores[s]))  
    print("Final score: " + str(total_score) + " points.")

main()