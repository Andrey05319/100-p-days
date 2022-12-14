import random
from art import logo


def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(list_with_cards):
    """Calculating users score"""
    sum_score = sum(list_with_cards)
    if sum_score == 21 and len(list_with_cards) == 2:
        return 0

    if 11 in list_with_cards and sum_score > 21:
        list_with_cards.append(1)
        list_with_cards.remove(11)
        return sum(list_with_cards)

    return sum_score


def compare(f_user_score, f_computer_score):
    user_wins = None
    if f_computer_score == 0:
        user_wins = False
    elif f_user_score == 0:
        user_wins = True
    elif f_user_score > 21:
        user_wins = False
    elif f_computer_score > 21:
        user_wins = True
    elif f_user_score > f_computer_score:
        user_wins = True
    elif f_computer_score > f_user_score:
        user_wins = False

    return user_wins


def play_blackjack():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        # computer_cards.append(deal_card())

    computer_cards.append(deal_card())
    computer_cards.append(11)

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score > 21 or user_score == 0 or computer_score == 0:
            is_game_over = True
        else:
            if input("Dou you want one more card? y/n: ").lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    game_result = compare(user_score, computer_score)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if game_result == True:
        print("You win")
    elif game_result == False:
        print("You lose")
    else:
        print("It's a draw")

    if input("Do you want to play blackjack again? y/n: ").lower() == "y":
        for _ in range(100):
            print("\n")
            play_blackjack()


print(logo)
play_blackjack()
