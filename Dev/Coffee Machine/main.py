import time
import os


MENU = {
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 50,
            "milk": 150
        },
        "cost": 1.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 7,
            "milk": 100
        },
        "cost": 2.50
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.75
    }

}
profit = 0
resources = {
    "milk": 300,
    "water": 500,
    "coffee": 50
}


is_on = True

def is_resurce_sufficient(order_ingredients):
    """Return True when order can be proceeded, False if ingredients are insufficient"""
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry, there is not enough {i}.")
            return False
        else:
            return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_succesful(money_received, drink_cost):
    """Return True when payment is accepted or False when money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources"""
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name}")




while is_on:
    choice = input("What coffee would you like to order? Espresso/Cappuccino/Latte: ").lower()
    if choice == "off":
        is_on = False
        break
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resurce_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
                time.sleep(2)

