
switch = True

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200
}

cost = {
    "espresso": 0.5,
    "cappuccino": 1.5,
    "latte": 2
}

def count_money(pennies, nickels, dimes, quarters):
    return pennies * .01 + nickels * 0.5 + dimes * .1 + quarters * .25

def print_report():
    return f"There is {resources['water']}ml of water, {resources['milk']}ml of milk, and {resources['coffee']}g of cofee"

def check_resources(drink):
    if drink == 'espresso':
        if resources['water'] <= 50:
            return "Sorry, not enough water."
        elif resources['coffee'] <= 18:
            return "Sorry, not enough coffee."
    if drink == 'latte':
        if resources['water'] <= 250:
            return "Sorry, not enough water."
        elif resources['coffee'] <= 24:
            return "Sorry, not enough coffee."
        elif resources['milk'] <= 150:
            return "Sorry, not enough milk."
    if drink == 'cappuccino':
        if resources['water'] <= 250:
            return "Sorry, not enough water."
        elif resources['coffee'] <= 24:
            return "Sorry, not enough coffee."
        elif resources['milk'] <= 100:
            return "Sorry, not enough milk."
def use_resources(drink):
    if drink == 'espresso':
        resources['water'] -= 50
        resources['coffee'] -= 15
    if drink == 'latte':
        resources['water'] -= 250
        resources['coffee'] -= 24
        resources['milk'] -= 150
    if drink == 'cappuccino':
        resources['water'] -= 250
        resources['coffee'] -= 24
        resources['milk'] -= 100

while switch:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    while choice not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        switch = False
    elif choice == 'report':
        print(print_report())
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    print("Please insert some coins")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How many nickels? "))
    pennies = float(input("How many pennies? "))
    amount = count_money(pennies, nickels, dimes, quarters)
    print(f"You have put in ${amount}")
    if cost[choice] < amount:
        change = amount - cost[choice]
        print(f"Enjoy your {choice}")
        print(f"Here is ${change} in change.")
        use_resources(choice)
    else:
        print(f"You haven't put in enough money. Take your {amount} back and try again.")

