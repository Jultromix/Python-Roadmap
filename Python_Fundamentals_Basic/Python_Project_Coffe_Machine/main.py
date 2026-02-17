"""This is the final project involving python fundamentals - 2025-12-31"""

from menu import show_menu
from orders import order_coffee
from history import show_history

def main():
    while True:
        # Show Menu
        show_menu()
        options = input("\nSelect an option:")

        if options == "1":
            order_coffee()
        elif options =="2":
            show_history()
        elif options == "3":
            # Saludar
            print("Thank you for trying our delicious coffees")
            break
        else:
            print("The option isn't valid, try again with a valid option")

if __name__ == "__main__":
    main()

    