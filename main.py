import data
import os

money = 0
program_run = True
prices = {'espresso': 1.5, 'latte': 2.5, 'cappuccino': 3.0}
VALUES = {'quarter': .25, 'dime': .1, 'nickel': .05, 'penny': .01}


def decimal_format(v):
    return "{:.2f}".format(v)


def make_drink(drink_type):
    drink = data.MENU[drink_type]
    if drink['water'] <= data.resources['water']:
        if drink['milk'] <= data.resources['milk']:
            if drink['coffee'] <= data.resources['coffee']:
                data.resources['water'] = data.resources['water'] - drink['water']
                data.resources['milk'] = data.resources['milk'] - drink['milk']
                data.resources['coffee'] = data.resources['coffee'] - drink['coffee']
                print("Here is your " + drink_type + "! ☕")
            else:
                print("Sorry there isn't enough coffee to make the " + drink_type + "!")
        else:
            print("Sorry there isn't enough milk to make the " + drink_type + "!")
    else:
        print("Sorry there isn't enough water to make the " + drink_type + "!")


def report():
    print(f"Water: {data.resources['water']}ml\nMilk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g\nMoney: ${money}")


def coins():
    print("\nPlease insert coins:")
    quarters = float(input("How many quarters do you have?: ")) * VALUES['quarter']
    dimes = float(input("How many dimes do you have?: ")) * VALUES['dime']
    nickels = float(input("How many nickels do you have?: ")) * VALUES['nickel']
    pennies = float(input("How many pennies do you have?: ")) * VALUES['penny']
    return quarters + nickels + dimes + pennies


def change(total_money, drink):
    return total_money - prices[drink]


while program_run:
    money = 0
    print('Prices: Espresso $1.50, Latte $2.50, Cappuccino $3.00')
    user = input('What would you like? (espresso/latte/cappuccino): ')
    if user.lower() == 'report':
        report()
    elif user.lower() == 'espresso':
        money = coins()
        if money >= prices['espresso']:
            print(f'Your change is $' + decimal_format(change(money, 'espresso')))
            make_drink('espresso')
        else:
            print("Change Ejected.... Please try again and put in required change.")
    elif user.lower() == 'off':
        break
    elif user.lower() == 'latte':
        money = coins()
        if money >= prices['latte']:
            print(f'Your change is $' + decimal_format(change(money, 'latte')))
            make_drink('latte')
        else:
            print("Change Ejected.... Please try again and put in required change.")
    elif user.lower() == 'cappuccino':
        money = coins()
        if money >= prices['cappuccino']:
            print(f'Your change is $' + decimal_format(change(money, 'cappuccino')))
            make_drink('cappuccino')
        else:
            print("Change Ejected.... Please try again and put in required change.")
    elif user.lower() == 'refill':
        data.resources = data.refill
