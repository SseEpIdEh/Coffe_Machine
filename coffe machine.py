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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough


def calculate_coin_value():
    print("please insert quarters?.")
    total = int(input("Enter the number of quarters: ")) * 0.25
    total += int(input("Enter the number of dimes: ")) * 0.10
    total += int(input("Enter the number of nickels: ")) * 0.05
    total += int(input("Enter the number of pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'here is $ {change} in change.')
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that is not enough money.money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'here is your {drink_name} ☕. enjoy!')


is_on = True
while is_on:
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    if ask == "off":
        is_on = False
        remain = 0
    elif ask == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"milk:  {resources['milk']}ml")
        print(f"coffee:  {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[ask]
        if is_resource_sufficient(drink["ingredients"]):
            payment = calculate_coin_value()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(ask, drink["ingredients"])
