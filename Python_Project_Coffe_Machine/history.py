ORDER_FILE = "orders.txt"

def show_history():
    try:
        print("\nThis is the history of prepared coffees:")
        with open(ORDER_FILE,"r",encoding="utf-8") as file:
            orders = file.readlines()
            if orders:
                for i,orders in enumerate(orders,start=1):
                    print(str(i) + ". " + orders.strip())
            else:
                print("There are no orders yet")

    except FileNotFoundError:
        print("There's not an available order history")
