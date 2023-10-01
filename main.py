from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

internal = ["off", "report"]

menu = Menu()
money = MoneyMachine()
res = CoffeeMaker()




while True:
    choice = input(f"What would you like?({menu.get_items()}):").lower()




    if choice in internal:
        if choice==internal[0]:
            exit()
            break

        if choice==internal[1]:
            print()
            res.report()
            money.report()
            print()
            continue
    
    if menu.find_drink(choice) is not None:
        item = menu.find_drink(choice)
        can_make = res.is_resource_sufficient(menu.find_drink(choice))

        if can_make:
            print()
            
            money.make_payment(menu.find_drink(choice).cost)

            res.make_coffee(item)
    

    
