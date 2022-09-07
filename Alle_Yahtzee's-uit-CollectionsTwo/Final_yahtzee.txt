# Amar Nagim
import random


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
          print("Je hebt een \"YAHTZEE\" gescoord!: 50 punten.\n\n")
          return 50

      elif ofAKind == 4 or ofAKind == 3:
          total = 0
          for index in range(5):
              total = total + int(dice[index])
          if ofAKind == 4:
              total = total + 10
              print("Je hebt een \"Four of a Kind\" gescoord!: " + str(total) + " punten.\n\n")
              return total
          else:
              noDuplicates = []
              for index in range(5):
                  if dice[index] not in noDuplicates:
                      noDuplicates.append(dice[index])
              if len(noDuplicates) == 2:
                  print("Je hebt \"Full House\" gescoord!: 25 punten.\n\n")
                  return 25
              else:
                  total=total+5
                  print("Je hebt een \"Three of a Kind\" gescoord!: " + str(total) + " punten.\n\n")
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
          print("Je hebt een \"Small Straight\" gescoord: 30 punten.\n\n")
          return 30
      elif straight ==5:
          print("Je hebt een \"Large Straight\" gescoord: 40 punten.\n\n")
          return 40
      else:
          return 0


  def noScore(dice):
      score = of_kind(dice)
      if score == 0:
        score = straight(dice)
      if score == 0:
        print("0 punten\n\n")
      return score



  def userGameplay():
      global totalScore
      totalScore = 0
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
      
          save = input("Welke dobbelstenen zou je opzij willen leggen? (1,2,3,4,5)")
          save = save.split(',')
          print("Roll 2: ", end ="")
          for x in range(5):
              if str(x + 1) not in save:
                  dice[x] = random.randint(1,6)
              if x < len(dice) - 1:
                  print(dice[x], end =" ")
              else:
                  print(dice[x])
          dice.sort()
          score = noScore(dice)
          totalScore = totalScore + score


  def endScreen():
    global totalScore
    global straight
    print("\n"*5,"Totale score:",totalScore)
    

  exit = input("Wil je Yahtzee spelen? (Y/N)")
  if exit == ("N") or exit == ("n"):
    print("Quit")
    break
  elif exit == ("Y") or exit == ("y"):
    print("\n"*5)
  elif exit == ("N") or exit == ("n"):
    print("Quit")
  else:
    print("Ongeldig antwoord....")
    break

    


  mainMenu()
  userGameplay()
  endScreen()
