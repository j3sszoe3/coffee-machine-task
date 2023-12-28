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

profit = 0
machine_on = True

def check_resource_levels(order_ingredients):
    '''function to compare required resources with actual resources'''
    enough_ingredients = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            enough_ingredients = False
    return enough_ingredients

def process_cash():
    '''function to process money'''
    print("Please insert coins:")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))

    total = float((quarters*0.25) + (dimes*0.1) + (nickles*0.05) +(pennies*0.01))
    return total
    
while machine_on:
    choice = input("What would you like? espresso/latte/cappuccino ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resource_levels(drink["ingredients"]): #checks if the output of resource function is TRUE
            payment = process_cash()
            drink_cost = float(drink["cost"]) #assigns the output of process_cash() function to a new variable
            if drink_cost > payment:
                print(f"Sorry, your payment of ${payment} is insufficient, please insert at least ${drink['cost']}.")
            elif payment > drink_cost:
                change = payment - drink_cost
                profit += drink_cost
                print(f"Thank you for your purchase. Your change is ${change}, enjoy your drink! ")
                choice1 = input("Choose 'y' to purchase another drink, or 'n' to exit.")
                if choice1 == 'n':
                    machine_on = False   
            else:
                profit += drink_cost
                print("Thank you for your purchase, enjoy your drink!")
                choice2 = input("Choose 'y' to purchase another drink, or 'n' to exit.")
                if choice2 == 'n':
                    machine_on = False
