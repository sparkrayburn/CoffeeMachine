from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



money_machine = MoneyMachine()
coffee_makeer = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()
is_on = True




while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_makeer.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_makeer.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_makeer.make_coffee(drink)



