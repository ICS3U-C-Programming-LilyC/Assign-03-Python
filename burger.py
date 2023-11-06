#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Nov/4/2023
# This program allows the user to buy a burger with 2 sizes, fries, and a drink.
# The program will print the subtotal, tax, and total cost of the purchase.

import constants


def main():
    # Declaring variables.
    # Allowing for the different prices of a burger to be under 1 variable.
    # Source: https://note.nkmk.me/en/python-multi-variables-values/#:~:text=You%20can%20assign%20multiple%20values,by%20separating%20them%20with%20commas%20%2C%20.&text=You%20can%20assign%20values%20to%20more%20than%20three%20variables%2C%20and,data%20types%20to%20those%20variables
    burger_prices = [0.00, 5.00, 7.00]
    fries_price = 3.00
    drink_price = 1.00
    subtotal = 0
    tax = 0
    total = 0

    # Initialize fries_as_integer and drink_as_integer and burger_size_as_integer with default values of 0.
    burger_size_as_integer = 0
    fries_as_integer = 0
    drink_as_integer = 0

    # Asking the user what size of burger they want.
    print("What size of burger do you want?")
    print("1 - Small")
    print("2 - Large")
    print("Enter the number representing the option you would like to select")
    print(
        "If you do not want to order a burger than press enter to proceed to the other menu options."
    )

    # Getting user input for burger size.
    burger_size = input("Enter your size of burger: ")

    # Initiating Try Catch.
    try:
        # Converting user input to an integer.
        burger_size_as_integer = int(burger_size)

        # If the user enters 1, the burger is $5.00.
        if burger_size_as_integer == 1:
            burger_price = 5.00

        # Else the user enters 2, the burger is $7.00.
        else:
            burger_price = 7.00

    # Catching any errors.
    except:
        print("Invalid choice for burger size.")

    # Asking the user if they want fries.
    print("Would you like fries?")
    print("1 - Yes")
    print("2 - No")
    print("Enter the number representing the option you would like to select.")
    print(
        "If you do not want to order fries than press enter to proceed to the other menu options."
    )

    # Getting user input for fries.
    fries_choice = input("Enter your choice for fries: ")

    try:
        # Converting user input to an integer.
        fries_as_integer = int(fries_choice)

        # If the user enters 1, the fries are $3.00.
        if fries_as_integer == 1:
            fries_price = 3.00

        # Else the user enters 2, the fries are $0.00.
        else:
            fries_price = 0.00

    # Catching any errors.
    except:
        print("Invalid choice for fries.")

    # Asking the user if they want a drink.
    print("Would you like a drink?")
    print("1 - Yes")
    print("2 - No")
    print("Enter the number representing the option you would like to select.")
    print(
        "If you do not want to order a drink than press enter to proceed to the other menu options."
    )

    # Getting user input for a drink.
    drink = input("Enter your choice for a drink: ")

    try:
        # Converting user input to an integer.
        drink_as_integer = int(drink)

        # If the user enters 1, the drink is $1.00.
        if drink_as_integer == 1:
            drink_price = 1.00

        # Else the user enters 2, the drink is $0.00.
        else:
            drink_price = 0.00

    # Catching any errors.
    except:
        print("Invalid choice for a drink.")

    # Calculating the subtotal, using if, elif and else statements for the several possibilities.
    # If the user wants a small burger, with fries and a drink.
    if burger_size_as_integer == 1 and fries_as_integer == 1 and drink_as_integer == 1:
        subtotal = burger_price + fries_price + drink_price

    # Else if the user wants a large burger, with fries and a drink.
    elif (
        burger_size_as_integer == 2 and fries_as_integer == 1 and drink_as_integer == 1
    ):
        subtotal = burger_price + fries_price + drink_price

    # Else if the user wants fries and a drink.
    elif fries_as_integer == 1 and drink_as_integer == 1:
        subtotal = fries_price + drink_price

    # Else if the user wants a small burger and a drink.
    elif burger_size_as_integer == 1 and drink_as_integer == 1:
        subtotal = burger_price + drink_price

    # Else if the user wants a large burger and a drink.
    elif burger_size_as_integer == 2 and drink_as_integer == 1:
        subtotal = burger_price + drink_price

    # Else if the user wants a small burger and fries.
    elif burger_size_as_integer == 1 and fries_as_integer == 1:
        subtotal = burger_price + fries_price

    # Else if the user wants a large burger and fries.
    elif burger_size_as_integer == 2 and fries_as_integer == 1:
        subtotal = burger_price + fries_price

    # Else if the user wants fries.
    elif fries_as_integer == 1:
        subtotal = fries_price

    # Else if the user wants a drink.
    elif drink_as_integer == 1:
        subtotal = drink_price

    # Else if the user wants a small burger.
    elif burger_size_as_integer == 1:
        subtotal = 5.00

    # Else if the user wants a large burger.
    elif burger_size_as_integer == 2:
        subtotal = 7.00

    # Else the user's order was not collected.
    else:
        print("We did not get your order. Please try again.")

    # Calculating tax.
    tax = subtotal * constants.TAX

    # Calculating total.
    total = subtotal + tax

    # Displaying the subtotal, tax, and total.
    print("Subtotal: ${:.2f}".format(subtotal))
    print("Tax: ${:.2f}".format(tax))
    print("Total: ${:.2f}".format(total))


if __name__ == "__main__":
    main()
