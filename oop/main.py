class Restaurant:

    def __init__(self):
        self.menu = {
            "burger": 75.00,
            "chickenjoy": 99.00,
            "spaghetti": 60.00,
            "fries": 50.00,
            "burger steak": 85.00,
            "peach mango pie": 45.00,
            "coke": 40.00
        }

        self.orders = []

    def display_menu(self):
        print()
        print("====================================")
        print("          WELCOME TO JOLLIBEE")
        print("====================================")
        print("MENU")

        for item, price in self.menu.items():
            print(item.title(), "- ₱{:.2f}".format(price))

        print("====================================")

    def display_order_options(self):
        print()
        print("1. Order")
        print("2. Exit")

    def display_another_order(self):
        print()
        print("Would you like to order another item?")
        print("1. Yes")
        print("2. No")

    def take_order(self):
        while True:
            self.display_menu()

            item_name = input("\nEnter Menu Item: ").lower()

            if item_name not in self.menu:
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

            price = self.menu[item_name]
            item_total = price * quantity

            self.orders.append(
                [item_name, quantity, price, item_total]
            )

            self.display_another_order()

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

    def calculate_total(self):
        subtotal = 0

        for order in self.orders:
            subtotal = subtotal + order[3]

        if subtotal >= 500:
            discount = subtotal * 0.10
        else:
            discount = 0

        final_total = subtotal - discount

        return subtotal, discount, final_total

    def display_receipt(self, subtotal, discount, final_total):
        print()
        print("====================================")
        print("             JOLLIBEE")
        print("          OFFICIAL RECEIPT")
        print("====================================")
        print("Item\t\tQty\tPrice\tTotal")
        print("------------------------------------")

        for order in self.orders:
            item = order[0]
            quantity = order[1]
            price = order[2]
            total = order[3]

            print("{}\t\t{}\t₱{:.2f}\t₱{:.2f}".format(
                item.title(), quantity, price, total))

        print("------------------------------------")
        print("Subtotal\t\t\t₱{:.2f}".format(subtotal))
        print("Discount\t\t\t₱{:.2f}".format(discount))
        print("Total\t\t\t\t₱{:.2f}".format(final_total))
        print("====================================")
        print("       THANK YOU FOR ORDERING!")
        print("====================================")


restaurant = Restaurant()

restaurant.display_menu()
restaurant.display_order_options()

while True:
    try:
        choice = int(input("Choose: "))

        if choice == 1:
            break
        elif choice == 2:
            print()
            print("Thank you for visiting Jollibee!")
            exit()
        else:
            print("Invalid choice. Please choose 1 or 2.")

    except ValueError:
        print("Please enter a number.")


restaurant.take_order()

subtotal, discount, final_total = restaurant.calculate_total()

restaurant.display_receipt(subtotal, discount, final_total)