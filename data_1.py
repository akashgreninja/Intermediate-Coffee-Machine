
from art import coffee
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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(coffee)
def is_resources_enough(is_ingredients_enough):
    for n in is_ingredients_enough:
        if is_ingredients_enough[n]>= resources[n]:
            print("OOPS,Shortage of resources contact someone")
            return False
    return True


def is_transaction_success(money_recieved,drink_cost):
    if money_recieved>= drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"here is your change of {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("not enough money")
        return False







def process_coins():
    """returns the total calculated """
    print("insert coins")
    total =int(input("how many quarters quarters"))*0.25
    total +=int(input("how many dines"))*0.10
    total +=int(input("how many nickles"))*0.05
    total +=int(input("how many pennies "))*0.01
    return total



def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"her is your {drink_name}")



game_over=False
while game_over==False:
    choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice=="off":
        game_over=True
    if choice =="report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Money :{profit}")
    else:
        drink=MENU[choice]
        # print(drink)
        if is_resources_enough(drink["ingredients"]):
           payment= process_coins()
           if is_transaction_success(payment,drink["cost"]):
               make_coffee(choice,drink["ingredients"])

           # if payment < drink["cost"]:
           #     print("not enough coins")
           #     game_over=False
           # else:
           #     profit+=drink["cost"]
           #     is
           #     print(profit)




