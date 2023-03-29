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


PROFIT = 0


def is_resource_sufficient(order_ingredients):
    """Returns TRUE when order can be made, FALSE if there are insufficient ingredients"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry! There is not enough {item}!")
            is_enough = False
    else:
        return is_enough


def process_coins():
    """ Calculates the amount of money inserted"""
    print("Please insert coins: ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many penniess? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, will return False is money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        global PROFIT
        PROFIT += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money! You will be refunded.")
        return False


def make_cofee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${PROFIT}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_cofee(choice, drink["ingredients"])
