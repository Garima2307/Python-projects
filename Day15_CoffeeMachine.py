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

def print_resources(dict):
    for key,value in dict.items():
        print(f"{key} : {value}")

def is_resource_sufficient(req_ingredients):
    for value in req_ingredients:
        if req_ingredients[value] > resources[value]:
            print(f"Sorry , enough {value} are not available !")
            return False
    return True

def process_coins():
    input("Please insert coins!!")
    total = int(input("How many quarters : "))*0.25
    total += int(input("How many dimes : "))*0.10
    total += int(input("How many nickels : "))*0.05
    total += int(input("How many pennies : "))*0.01
    return total

def transaction_successful(payment_received , drink_cost):
    if payment_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(payment_received - drink_cost , 2)
        print(f"Here is ${change} in change.")
        return True

    else :
        print("Sorry ! That's not enough money . Money refunded.")
        return False

def make_coffee(drink_chosen , order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

drink_need = True
money_spent_by_user = 0
while drink_need:
    drink_name = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink_name == "off":
        print("Coffee machine has been successfully turned-off. So , no further orders will be available!")
        drink_need = False
        break
    elif drink_name == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else :
        drink = MENU[drink_name]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment , drink["cost"]):
                make_coffee(drink_name , drink["ingredients"])







