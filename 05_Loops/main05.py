# FOR LOOP ************************************************************************************

# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "pie")

# AVERAGE HEIGHT ************************************************************************************

# #156 178 165 171 187
#
# sum_of_heights = 0
# number_of_students = 0
#
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#   sum_of_heights = sum_of_heights + student_heights[n]
#   number_of_students = number_of_students + 1
#
# average_height = sum_of_heights/number_of_students
#
# print(f"Average height is {average_height}")

# MAX SCORE ************************************************************************************

# #156 178 165 171 187

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# max_score = 0
#
# for score in student_scores:
#     if score > max_score:
#         max_score = score
#
# print(f"Max score is {max_score}")

# GAUSSE TASK ************************************************************************************

# total = 0
# for number in range(1, 101):
#     total += number
#
# print(total)

# ADDING EVEN NUMBERS ************************************************************************************

# sum_of_even_numbers = 0
#
# for number in range(1, 101):
#     if number % 2 == 0:
#         sum_of_even_numbers = sum_of_even_numbers + number
#
# print(sum_of_even_numbers)

# FIZZ BUZZ ************************************************************************************

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# PASSWORD GENERATOR ************************************************************************************

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''

for n in range(1, (nr_letters + 1)):
    random_letter = str(random.choice(letters))
    password = password + random_letter

for n in range(1, (nr_numbers + 1)):
    random_number = str(random.choice(numbers))
    password = password + random_number

for n in range(1, (nr_symbols + 1)):
    random_symbol = str(random.choice(symbols))
    password = password + random_symbol

print(password)

list_password = list(password)
random.shuffle(list_password)

print(list_password)

result_password = ''.join(list_password)

print(result_password)