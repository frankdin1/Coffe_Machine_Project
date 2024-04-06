MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

#TODO 1. Create different options for different requests that users might have
# a. Option for user to see all their options.
# b. Option for user to choose what type of coffee they would like.
# c. Option for user see menu.
# d. Option to see machine resources left over.

#TODO 2. Create sequence of events after user chooses what type of coffee they want
# a. if user selects a coffee type, set a target price to be the price of the coffee choice
# b. ask for user coins for each denomination and sum them up
# c. if the sum of user coins is equal to or greater than the target price,
# display the correct change and display a message with their coffee choice
# d. if the sum of user coins is less than the target price, inform the user that
# he needs more money
# e. when a user chooses their coffee type, check whether there are enough resources to make
# 1 cup of coffee
# f. if a user chooses a coffee type but there are not enough resources to make the coffee, the loop should go back to
# the original menu


total_earnings = 0


def print_menu():
    print("Espresso:\nIngredients:\n\tWater: 50mL\n\tCoffee: 18mL\nPrice: $1.50")
    print("\nLatte:\nIngredients:\n\tWater: 200mL\n\tCoffee: 24mL\n\tMilk: 150mL\nPrice: $2.50")
    print("\nCappuccino:\nIngredients:\n\tWater: 250mL\n\tCoffee: 24mL\n\tMilk: 100mL\nPrice: $2.50")


def show_available_resources():
    print(f"Water: {resources["water"]}mL")
    print(f"Coffee: {resources["coffee"]}mL")
    print(f"Milk: {resources["milk"]}mL")


def print_machine_report():
    print("-- Report --\n")
    print(f"Water: {resources["water"]}mL")
    print(f"Coffee: {resources["coffee"]}mL")
    print(f"Milk: {resources["milk"]}mL")
    print(f"Money: ${total_earnings}")


def coffee_choice(coffee_type):
    price = 0
    #if coffee_type == 'espresso':
    # if resources["water"] < MENU[coffee_type]["ingredients"]["water"] or \
    #         resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"] or \
    #         resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
    if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
        print("Sorry, there's not enough water.")
    elif resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        print("Sorry, there's not enough coffee.")
    elif resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        print("Sorry, there's not enough milk.")
    else:
        print(f"Price: ${MENU[coffee_type]["cost"]}")
        price = MENU[coffee_type]["cost"]
    return price


def insert_coins():
    payment = 0
    print("Please insert coins")
    quarter_count = int(input("How many quarters?: "))
    quarter_amount = 0.25 * quarter_count
    payment += quarter_amount

    dime_count = int(input("How many dimes?: "))
    dime_amount = 0.10 * dime_count
    payment += dime_amount

    nickel_count = int(input("How many nickels?: "))
    nickel_amount = 0.05 * nickel_count
    payment += nickel_amount

    penny_count = int(input("How many pennies?: "))
    penny_amount = 0.01 * penny_count
    payment += penny_amount

    return payment

def make_coffee(coffee_type):
    #if coffee == 'espresso':
    if resources["water"] - MENU[coffee_type]["ingredients"]["water"] >= 0:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    else:
        resources["water"] = 0
    if resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"] > 0:
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    else:
        resources["coffee"] = 0
    if resources["milk"] - MENU[coffee_type]["ingredients"]["milk"] > 0:
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    else:
        resources["milk"] = 0


while True:
    total_payment = 0
    print("What would you like to do?")
    print("1 - Menu\n2 - Resources\n3 - Report\n4 - Coffee\n5 - Off")
    choice = int(input())
    if choice == 1:
        print_menu()
    elif choice == 2:
        show_available_resources()
    elif choice == 3:
        print_machine_report()
    elif choice == 4:
        coffee = input("What would you like? Espresso? Latte? Cappuccino?").lower()
        target_price = coffee_choice(coffee)
        if target_price == 0:
            break
        total_payment = insert_coins()

        if target_price <= total_payment:
            total_earnings += total_payment
            print(f"Your change is {total_payment - target_price}")
            make_coffee(coffee)
            # if coffee == 'espresso':
            #     resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            #     resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            # elif coffee == 'latte':
            #     resources["water"] -= MENU["latte"]["ingredients"]["water"]
            #     resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            #     resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            # elif coffee == 'cappuccino':
            #     resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            #     resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            #     resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        else:
            print("You didn't insert enough money. Money refunded.")

    elif choice == 5:
        break
