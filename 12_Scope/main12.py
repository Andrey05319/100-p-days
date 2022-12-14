# ---- SCOPE -----------------------------------------------------------

# enemies = 1
#
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
# # will be printed:
# # enemies inside function: 2
# # enemies outside function: 1

# ---- LOCAL SCOPE -----------------------------------------------------------

# def drink_potion():
#   potion_strenght = 2
#   print(potion_strenght)
#
# drink_potion()
# #print(potion_strenght) # It will generate a mistake

# ---- GLOBAL SCOPE -----------------------------------------------------------

# enemies = 1
#
# def increase_enemies():
#   global enemies
#   enemies += 1
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# ---- NUMBER GUESSING GAME -----------------------------------------------------------

import random
from art import logo

print(logo)

def guessing(f_attempts):
    if f_attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == guessed_number:
            print(f"You got it! The answer was {guessed_number}")
            return
        elif guess > guessed_number:
            print(f"Too high.")
            f_attempts -= 1
            print(f"You still have {f_attempts} attempts.")
            guessing(f_attempts)
        elif guess < guessed_number:
            print(f"Too low.")
            f_attempts -= 1
            print(f"You still have {f_attempts} attempts.")
            guessing(f_attempts)
        else:
            print(f"Wrong input.")
            print(f"You still have {f_attempts} attempts.")
            guessing(f_attempts)
    else:
        print("You are out of attempts. You loose.")
        return



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

guessed_number = random.randint(1, 100)

print(f"Pssst, the correct answer is {guessed_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

guessing(attempts)

