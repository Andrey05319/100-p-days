# ******* Function with outputs ***********************************************************************

# def format_name(f_name, l_name):
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f"{f_name} {l_name}"
#
# formatted_string = format_name("AnDrEy", "PiCARD")
# print(formatted_string)

# ******* Function with outputs ***********************************************************************


# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You did not provide valid inputs"
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f"{f_name} {l_name}"
#
# formated_string = format_name("AnDrEy", "")
# print(formated_string)

# ******* DAYS IN MONTH ***********************************************************************


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(input_year, input_month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     leap_year = is_leap(input_year)
#
#     if leap_year == True and input_month == 2:
#         return 29
#     else:
#         return month_days[input_month - 1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# ******* DOCSTRINGS ***********************************************************************

# def format_name(f_name, l_name):
#     """Take the first and the last name and format it to return the title case version"""
#     if f_name == "" or l_name == "":
#         return "You did not provide valid inputs"
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f"{f_name} {l_name}"
#
# formated_string = format_name("AnDrEy", "")
# print(formated_string)

# ******* CALCULATOR ***********************************************************************

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What is the first number?: "))

    want_to_continue = True

    while want_to_continue:

        for oper in operations:
            print(oper)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operation_symbol](num1, num2)

        print((f"{num1} {operation_symbol} {num2} = {answer}"))

        want_to_continue_input = input(f"Do you want to continue calculations with {answer}. Type y for Yes or n for No: ").lower()
        if want_to_continue_input == "n":
            want_to_continue = False
            calculator()
        else:
            num1 = answer

calculator()

