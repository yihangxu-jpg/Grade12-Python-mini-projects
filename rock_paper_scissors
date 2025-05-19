import random
# import module

actions = [-1, 0, 1]
# use numbers to represent actions

pts = 0
# set initial score to 0

def decider(x,y,z): # define a function of deciding who's winning
  if (x or y == 1) and (x or y == -1):
    x = x * (-1)
    y = y * (-1)
  # in order to deal with exceptions.
  # for example the player chose rock(-1) and computer chose scissors(1); rock should beat scissors, but since -1 < 1, the computer wins. Therefore, at instances like this, we should reverse the numbers to make rock > scissors.

  if x == y:
    print("ur choice is:", user_choice)
    print("computer's choice is:", comp_choice)
    print("therefore, it's a tie")
    z += 0
    print("ur current score is:", z)
    return z
# tie
  
  if x > y:
    print("ur choice is:", user_choice)
    print("computer's choice is:", comp_choice)
    print("therefore, you won")
    z += 1
    print("ur current score is:", z)
    return z
# win
  
  if x < y:
    print("ur choice is:", user_choice)
    print("computer's choice is:", comp_choice)
    print("therefore, you lost")
    z -= 1
    print("ur current score is:", z)
    return z
#lost

# main body of the game
while True:
  comp_choicenum = random.randint(-1,1)
  # generating random number
  user_choice = input("plz enter 'rock', 'paper', or 'scissors'")
  user_choice = user_choice.lower()
  while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
    print("invalid input, plz try again")
    user_choice = input("plz enter 'rock', 'paper', or 'scissors'")
    user_choice = user_choice.lower()
  # asking user to input rock, paper, or scissors

  
  user_choicenum = user_choice
  if user_choice == "rock":
    user_choicenum = actions[0]
  if user_choice == "paper":
    user_choicenum = actions[1]
  if user_choice == "scissors":
    user_choicenum = actions[2]
  # storing user's choice as a number

  if comp_choicenum == -1:
    comp_choice = "rock"
  if comp_choicenum == 0:
    comp_choice = "paper"
  if comp_choicenum == 1:
    comp_choice = "scissors"
  # in order to tell user the result, convert the random number into corresponding English words
  
  pts = decider(user_choicenum, comp_choicenum, pts)

  if input("press any button to continue; to quit game, plz type 'stop'").lower() == "stop":
    break
  



  
