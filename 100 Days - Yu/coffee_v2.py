
switch = True

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200
}

drinks = {
    "espresso": {
        "cost": 0.5,
        "ingredients": {
            "water": 50,
            "coffee": 15,
        }
    },
    "cappuccino": {
        "cost": 1.5,
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 150
        }
    },
    "latte": {
        "cost": 1,
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        }
    }
}

#TODO Make sure we figure this out
def count_money(pennies, nickels, dimes, quarters):
    return pennies * .01 + nickels * 0.5 + dimes * .1 + quarters * .25

def print_report():
    return f"There is {resources['water']}ml of water, {resources['milk']}ml of milk, and {resources['coffee']}g of cofee"

def check_resources(drink):
    for ingredient, amount in drinks[drink]['ingredients'].items():
        if resources[ingredient] < amount:
            return f"Sorry, not enough {ingredient}."
    return None

def use_resources(drink):
    for ingredient, amount in drinks[drink]['ingredients'].items():
        resources[ingredient] -= amount


while switch:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    while choice not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        switch = False
    elif choice == 'report':
        print(print_report())
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    enough = check_resources(choice)
    if enough:
        print(enough)
    else:
        print("Please insert some coins")

        quarters = float(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickels = float(input("How many nickels? "))
        pennies = float(input("How many pennies? "))
        amount = count_money(pennies, nickels, dimes, quarters)
        print(f"You have put in ${amount}")
        if drinks[choice]['cost'] < amount:
            change = amount - drinks[choice]['cost']
            print(f"Enjoy your {choice}")
            print(f"Here is ${change} in change.")
            use_resources(choice)
        else:
            print(f"You haven't put in enough money. Take your {amount} back and try again.")

