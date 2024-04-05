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

while True:
    print("What would you like to do?")
    print("1 - Menu\n2 - Resources\n3 - Report\n4 - Coffee\n5 - Off")
    choice = int(input())
    if choice == 1:
        print("Espresso:\nIngredients:\n\tWater: 50mL\n\tCoffee: 18mL\nPrice: $1.50")
        print("\nLatte:\nIngredients:\n\tWater: 200mL\n\tCoffee: 24mL\n\tMilk: 150mL\nPrice: $2.50")
        print("\nCappuccino:\nIngredients:\n\tWater: 250mL\n\tCoffee: 24mL\n\tMilk: 100mL\nPrice: $2.50")
    elif choice == 2:
        print(resources)
    elif choice == 3:
        print("Report")
    elif choice == 4:
        total_payment = 0
        target_price = 0
        total_earnings = 0
        coffee = input("What would you like? Espresso? Latte? Cappuccino?").lower()
        if coffee == 'espresso':
            target_price = MENU["espresso"]["cost"]
        elif coffee == 'latte':
            target_price = MENU["latte"]["cost"]
        elif coffee == 'cappuccino':
            target_price = MENU["cappuccino"]["cost"]

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

        penny_count = int(input("How many pennie?: "))
        penny_amount = 0.01 * penny_count
        total_payment += penny_amount

        if target_price <= total_payment:
            total_earnings += total_payment
            print(f"Your change is {total_payment - target_price}")
        else:
            print("You didn't insert enough money.")

    elif choice == 5:
        break
