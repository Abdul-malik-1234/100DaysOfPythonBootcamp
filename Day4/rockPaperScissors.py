# The Basic Rules of RPS

# Despite its underlying complexity, the game’s rules are straightforward. Players deliver hand signals representing rock, paper, or scissors, with the outcome determined by these three rules:

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice=int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2:"))
if user_choice==0:
    print("You choose: Rock")
    print(rock)
elif user_choice==1:
    print("You choose: Paper")
    print(paper)
else:
    print("You choose: Scissors")
    print(scissors)
computer_choice=random.randint(0,2)
if computer_choice==0:
    # computer->Rock
    print("The computer choose: Rock")
    print(rock)
    if user_choice==1:
        #user-> paper 
        print("You win!")
    elif user_choice==0:
        #user->rock
        print("It's a draw!")
    else:
        #user->scissors
        print("You loose to computer!")
elif computer_choice==1:
    #computer-> paper
    print("The computer choose: Paper")
    print(paper)
    if user_choice==1:
        #user->paper
        print("It's a draw!")
    elif user_choice==0:
        #user->rock
        print("You loose!" )
    else:
        #user->scissors
        print("You win!")
elif computer_choice==2:
    # computer:scissors
    print("The computer choose: Scissors")
    print(scissors)
    if user_choice==1:
        # user->paper
        print("You loose!")
    elif user_choice==0:
        #user->rock
        print("You win!")
    else:
        #user:scissors
        print("It's a draw!")
    