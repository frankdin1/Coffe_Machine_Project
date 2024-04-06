MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


def coffee_choice(coffee_type, price):
    #if coffee_type == 'espresso':
    if resources["water"] < MENU[coffee_type]["ingredients"]["water"] or \
            resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"] or \
            resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        print(f"Not enough ingredients to make a(n) {coffee_type}.")
        return
    else:
        print(f"Price: ${MENU[coffee_type]["cost"]}")
        price = MENU[coffee_type]["cost"]


while True:
    target_price = 0
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
        coffee_choice(coffee, target_price)
        # if coffee == 'espresso':
        #     if resources["water"] < MENU["espresso"]["ingredients"]["water"] or resources["coffee"] < \
        #             MENU["espresso"]["ingredients"]["coffee"]:
        #         print("Not enough ingredients to make an espresso.")
        #         break
        #     else:
        #         print(f"Price: ${MENU["espresso"]["cost"]}")
        #         target_price = MENU["espresso"]["cost"]
            # if resources["water"] < MENU["espresso"]["ingredients"]["water"] or resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            #     print("Not enough to make an espresso.")
            #     break
        # elif coffee == 'latte':
        #     if resources["water"] < MENU["latte"]["ingredients"]["water"] or resources["coffee"] < \
        #             MENU["latte"]["ingredients"]["coffee"] or resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
        #         print("Not enough ingredients to make a latte.")
        #         break
        #     else:
        #         print(f"Price: ${MENU["latte"]["cost"]}")
        #         target_price = MENU["latte"]["cost"]
        #     # if resources["water"] < MENU["latte"]["ingredients"]["water"] or resources["coffee"] < \
        #     #         MENU["latte"]["ingredients"]["coffee"] or resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
        #     #     print("Not enough to make a latte.")
        #     #     break
        # elif coffee == 'cappuccino':
        #     print(f"Price: ${MENU["cappuccino"]["cost"]}")
        #     target_price = MENU["cappuccino"]["cost"]
        #     if resources["water"] < MENU["cappuccino"]["ingredients"]["water"] or resources["coffee"] < \
        #             MENU["cappuccino"]["ingredients"]["coffee"] or resources["milk"] < \
        #             MENU["cappuccino"]["ingredients"]["milk"]:
        #         print("Not enough ingredients to make a cappuccino.")
        #         break

        print("Please insert coins")
        quarter_count = int(input("How many quarters?: "))
        quarter_amount = 0.25 * quarter_count
        total_payment += quarter_amount

        dime_count = int(input("How many dimes?: "))
        dime_amount = 0.10 * dime_count
        total_payment += dime_amount

        nickel_count = int(input("How many nickels?: "))
        nickel_amount = 0.05 * nickel_count
        total_payment += nickel_amount

        penny_count = int(input("How many pennies?: "))
        penny_amount = 0.01 * penny_count
        total_payment += penny_amount

        if target_price <= total_payment:
            total_earnings += total_payment
            print(f"Your change is {total_payment - target_price}")
            if coffee == 'espresso':
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            elif coffee == 'latte':
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            elif coffee == 'cappuccino':
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        else:
            print("You didn't insert enough money. Money refunded.")

    elif choice == 5:
        break

print("line outside while loop")
