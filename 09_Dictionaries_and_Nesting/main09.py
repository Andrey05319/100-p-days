# *********** DICTIONARIES ***************************************************
#
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# print(programming_dictionary["Bug"])
#
# # Adding new items to dictionary
#
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)
#
# # Edit an item in dictionary
#
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)
#
# # Loop through dictionary
#
# for thing in programming_dictionary:
#     print(thing)  # You will get keys only
#     print(programming_dictionary[thing])  # You will get the value

# *********** Student grades ***************************************************


# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
#
# def score_to_grade_converter(score):
#     # This is the scoring criteria:
#     # > Scores 91 - 100: Grade = "Outstanding"
#     # > Scores 81 - 90: Grade = "Exceeds Expectations"
#     # > Scores 71 - 80: Grade = "Acceptable"
#     # > Scores 70 or lower: Grade = "Fail"
#
#     score = student_scores[student]
#     grade = ""
#     if score >= 91 and score <= 100:
#         grade = "Outstanding"
#     elif score >= 81 and score <= 90:
#         grade = "Exceeds Expectations"
#     elif score >= 71 and score <= 80:
#         grade = "Exceeds Expectations"
#     elif score <= 70:
#         grade = "Fail"
#
#     return (grade)
#
#
# for student in student_scores:
#     student_grades[student] = score_to_grade_converter(student_scores[student])
#
# print(student_grades)

# *********** Nesting ***************************************************

# # Regular dictionary
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
#
# # Nesting a list in a dictionary
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
#
# print(travel_log["Germany"][1])
#
# # Nesting dictionary in a dictionary
#
# travel_log_2 = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 15},
# }
#
# print(travel_log_2["France"]["cities_visited"][1])
#
# # Nesting dictionary in a list
#
# travel_log_2 = [
#     {"country": "France",
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "total_visits": 12},
#     {"country": "Germany",
#      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#      "total_visits": 15},
# ]

# *********** Dictionary in list Challenge ***************************************************

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
#
# def add_new_country(country, visits, cities):
#     new_country = {
#         "country": country,
#         "visits": visits,
#         "cities": cities,
#     }
#     travel_log.append(new_country)
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# *********** Blind Auction ***************************************************

# from replit import clear

from art import logo


print(logo)

def new_participant():
    name = input("What is your name? ")
    bid = float(input("What is your bid? "))
    all_participants[name] = bid


all_participants = {}
auction_is_not_finished = True
while auction_is_not_finished:
    new_participant()

    input_is_correct = True
    while input_is_correct:
        is_there_any_more_participants = input("Is there any more participants? Yes/No ").lower()
        if is_there_any_more_participants == "no":
            auction_is_not_finished = False
            input_is_correct = False
        elif is_there_any_more_participants == "yes":
            input_is_correct = False
        else:
            print("Wrong input. Try again.")

#print(all_participants)

highest_bid = 0
winner_name = ""

for key in all_participants:
    if all_participants[key] > highest_bid:
        highest_bid = all_participants[key]
        winner_name = key

print(f"Winner is {winner_name} with a bid of {highest_bid}")
