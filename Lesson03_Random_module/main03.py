# Random module **************************************************************

# import random
# #import my_module
#
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# #print(my_module.pi)
#
# random_float = random.random()
# print(random_float)

# Heads or tails **********************************************************************************
#
# # You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# # **Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# # There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
# #
# # e.g.
# # 1 means Heads
# # 0 means Tails
#
# import random
#
# head_or_tail = random.randint(0,1)
#
# if head_or_tail == 1:
#     print("Heads")
# else:
#     print("Tails")

# LISTS **********************************************************************************

# states_of_america = ["Delaware", "Pennsylvania", "Ohio"]

# WHO IS PAYING FOR THE BILL **********************************************************************************

# import random
#
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# number_of_persons = len(names)
#
# random_number = random.randint(0, (number_of_persons - 1))
#
# print(f"Today {names[random_number]} will pay for the bill")


# TREASURE MAP **********************************************************************************

# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# column = int(position[0])-1
# line = int(position[1])-1
#
# map[line][column] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")

# ROCK PAPER SCISSORS **********************************************************************************

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

possible_variants = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice = random.randint(0, 2)

print(f"Your choiсe: \n {possible_variants[player_choice]}")

print(f"Computer choiсe \n {possible_variants[computer_choice]}")

if (player_choice == computer_choice):
    print("It's a draw")
elif (player_choice == 0 and computer_choice ==1) or (player_choice == 1 and computer_choice ==0) or (player_choice == 2 and computer_choice ==0):
    print("You loose")
else:
    print("You win")


