# Simple function ***************

# def greet():
#     print("Do this")
#     print("Do also this")
#     print("And this")
#
#
# greet()

# Function that allows for input ***************

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#
# greet_with_name("Andrey")

# Function with more than 1 input ***************

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is like in {location}?")
#
#
# greet_with(name="Andrey", location="London")

# *************  Wall painting calculator ********************************************************

# Define a function called paint_calc() so that the code below works.

# import math
#
# def paint_calc(height, width, cover):
#
#     number_of_cans_without_rounding = (height * width)/5
#     #print(number_of_cans_without_rounding)
#     rounded_number_of_cans = math.ceil(number_of_cans_without_rounding)
#     print(f"You need {rounded_number_of_cans} cans of paint to paint the wall")
#
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# *************  Prime Number Checker ********************************************************

# def prime_checker(number):
#     number_is_prime = True
#
#     for i in range(2, number):
#         if number % i == 0:
#             number_is_prime = False
#
#     if number_is_prime:
#         print(f"{number} is the Prime Number")
#     else:
#         print(f"{number} is not the Prime Number")
#
#
# n = int(input("Check this number: "))
# prime_checker(number=n)

# *************  Caesar Cipher - MY VERSION ********************************************************
#

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
# def encrypt(text, shift):
#     encrypted_message = ""
#
#     for letter in text:
#         if letter not in alphabet:
#             encrypted_message = encrypted_message + letter
#         else:
#             letter_index = alphabet.index(letter)
#             # print(f"letter index = {letter_index}")
#
#             if (letter_index + shift) < len(alphabet):
#                 encrypted_message = encrypted_message + alphabet[letter_index + shift]
#             else:
#                 encrypted_message = encrypted_message + alphabet[len(alphabet) - (letter_index + shift)]
#
#     print(f"Encripted text: {encrypted_message}")
#
#
# def decrypt(text, shift):
#     decrypted_message = ""
#
#     for letter in text:
#         if letter not in alphabet:
#             decrypted_message = decrypted_message + letter
#         else:
#             letter_index = alphabet.index(letter)
#             # print(f"letter index = {letter_index}")
#
#             if (letter_index - shift) > 0:
#                 decrypted_message = decrypted_message + alphabet[letter_index - shift]
#             else:
#                 decrypted_message = decrypted_message + alphabet[len(alphabet) + (letter_index - shift)]
#
#     print(f"Encripted text: {decrypted_message}")
#
#
# if direction == "encode":
#     encrypt(text=text, shift=shift)
# elif direction == "decode":
#     decrypt(text=text, shift=shift)
# else:
#     print("There is no such action in this program")

# *************  Caesar Cipher - Angela's version ********************************************************

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")



