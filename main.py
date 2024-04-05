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

print("What would you like to do?")
print("1 - Menu\n2 - Resources\n3 - Report\n4 - Coffee")
choice = int(input())
if choice == 1:
    print(MENU)
elif choice == 2:
    print(resources)
elif choice == 3:
    print("Report")
elif choice == 4:
    print("Coffee")