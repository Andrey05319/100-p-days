# Coffee machine ----------------------------------

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def process_coins(coffee_type):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    quarters_nominal = 0.25
    dimes_nominal = 0.10
    nickles_nominal = 0.05
    pennies_nominal = 0.01

    inputed_money = quarters * quarters_nominal + dimes * dimes_nominal + nickles * nickles_nominal + pennies * pennies_nominal

    if inputed_money < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        change = float("{0:.2f}".format(inputed_money - MENU[coffee_type]["cost"]))
        print(f'Here is ${change} in change.')
        return MENU[coffee_type]["cost"]


def report(money_res, resources_res):
    print(f"Water: {resources_res['water']}ml")
    print(f"Milk: {resources_res['milk']}ml")
    print(f"Coffee: {resources_res['coffee']}g")
    print(f"Money: ${money_res}")
    print(f"\n")


def make_coffee(money_in_machine, recourses_in_machine):
    user_coffee_choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()

    if user_coffee_choice == "off":
        return

    if user_coffee_choice == "report":
        report(money_in_machine, recourses_in_machine)
        make_coffee(money_in_machine, recourses_in_machine)

    coffee_types = ["espresso", "latte", "cappuccino"]
    if user_coffee_choice not in coffee_types:
        print("We do not have this type of coffee. Try again.")
        make_coffee(money_in_machine, recourses_in_machine)

    money_inputed = process_coins(user_coffee_choice)
    if money_inputed == 0:
        make_coffee(money_in_machine, recourses_in_machine)

    if (recourses_in_machine["water"] - MENU[user_coffee_choice]["ingredients"]["water"]) < 0:
        print("Sorry there is not enough water")
        make_coffee(money_in_machine, recourses_in_machine)
    elif (recourses_in_machine["milk"] - MENU[user_coffee_choice]["ingredients"]["milk"]) < 0:
        print("Sorry there is not enough milk")
        make_coffee(money_in_machine, recourses_in_machine)
    elif (recourses_in_machine["coffee"] - MENU[user_coffee_choice]["ingredients"]["coffee"]) < 0:
        print("Sorry there is not enough coffee")
        make_coffee(money_in_machine, recourses_in_machine)

    print(f"Here is your {user_coffee_choice} ☕️.Enjoy!")

    recourses_in_machine_after_making_coffee = {
        "water": (recourses_in_machine["water"] - MENU[user_coffee_choice]["ingredients"]["water"]),
        "milk": (recourses_in_machine["milk"] - MENU[user_coffee_choice]["ingredients"]["milk"]),
        "coffee": (recourses_in_machine["coffee"] - MENU[user_coffee_choice]["ingredients"]["coffee"]),
    }

    money_in_machine_after_making_coffee = money_in_machine + money_inputed

    make_coffee(money_in_machine_after_making_coffee, recourses_in_machine_after_making_coffee)


make_coffee(money, resources)

# TODO 1
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# TODO 2
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

# TODO 3
# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# TODO 4
# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

# TODO 5
# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO 6
# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

# TODO 7
# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink


# ------- ANGELA'S VERSION ------------------------------------------------------------------

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]  # Мне тут не понятно как из функции модифицируется глобальная переменная без объявления ее глобальной
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])












