def display_order_options():
    print()
    print("1. Order")
    print("2. Exit")


def display_another_order():
    print()
    print("Would you like to order another item?")
    print("1. Yes")
    print("2. No")


def take_order(menu, orders):
    while True:
        print()
        print("Available Menu:")

        for item, price in menu.items():
            print(item.title(), "- ₱{:.2f}".format(price))

        item_name = input("\nEnter Menu Item: ").lower()

        if item_name not in menu:
            print("Item not found. Please choose from the menu.")
            continue

        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

        except ValueError:
            print("Please enter a valid quantity.")
            continue

        price = menu[item_name]
        item_total = price * quantity

        orders.append([item_name, quantity, price, item_total])

        display_another_order()

        while True:
            try:
                another_order = int(input("Choose: "))

                if another_order == 1:
                    break
                elif another_order == 2:
                    return
                else:
                    print("Invalid choice. Please choose 1 or 2.")

            except ValueError:
                print("Please enter a number.")