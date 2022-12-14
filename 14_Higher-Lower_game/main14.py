import random
from art import logo, vs
from game_data import data

starting_score = 0


def compare_function(item_A_to_compare, current_score):
    print(
        f"Compare A: {item_A_to_compare['name']}, a {item_A_to_compare['description']}, from, {item_A_to_compare['country']}")
    print(vs)

    items_are_different = False
    while not items_are_different:
        item_B_to_compare = random.choice(data)
        if item_B_to_compare != item_A_to_compare:
            items_are_different = True

    print(
        f"Compare B: {item_B_to_compare['name']}, a {item_B_to_compare['description']}, from, {item_B_to_compare['country']}")

    print(
        f"Pssss... A has {item_A_to_compare['follower_count']} followers and B has {item_B_to_compare['follower_count']} followers")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if item_A_to_compare['follower_count'] >= item_B_to_compare['follower_count'] and user_choice == "a":
        current_score = current_score + 1
        print(f"You're right! Current score: {current_score}.")
        print("\n")
        compare_function(item_A_to_compare, current_score)
    elif item_A_to_compare['follower_count'] <= item_B_to_compare['follower_count'] and user_choice == "b":
        current_score = current_score + 1
        print(f"You're right! Current score: {current_score}.")
        print("\n")
        compare_function(item_B_to_compare, current_score)
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")


print(logo)

fist_item_to_compare = random.choice(data)

compare_function(fist_item_to_compare, starting_score)
