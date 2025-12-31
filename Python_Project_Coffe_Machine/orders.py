ORDER_FILE = "orders.txt"

def order_coffee():
    print("\n Choose your coffee:")
    print("1. Expresso")
    print("2. Latte")
    print("3. Matcha")
    print("4. Mochaccino")
    print("5. Cold Brew")

    option = input("Select option:")

    coffees = {
        "1" : "Expresso",
        "2" : "Latte",
        "3" : "Matcha",
        "4" : "Mochaccino",
        "5" : "Cold Brew",
    }

    if option in coffees:
        choosen_coffe = coffees[option]
        print("You have selected " + choosen_coffe + ". Preparing your coffee")
        
        with open(ORDER_FILE,"a", encoding="utf-8") as file:
            file.write(choosen_coffe + "\n")
    else:
        print("the option isn't valid, try again")