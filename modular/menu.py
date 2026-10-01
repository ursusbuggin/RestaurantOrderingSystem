menu = {
    "burger": 75.00,
    "chickenjoy": 99.00,
    "spaghetti": 60.00,
    "fries": 50.00,
    "burger steak": 85.00,
    "peach mango pie": 45.00,
    "coke": 40.00
}


def display_menu():
    print()
    print("====================================")
    print("          WELCOME TO JOLLIBEE")
    print("====================================")
    print("MENU")

    for item, price in menu.items():
        print(item.title(), "- ₱{:.2f}".format(price))

    print("====================================")