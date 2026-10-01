from menu import menu, display_menu
from ordering import display_order_options, take_order
from receipt import calculate_total, display_receipt


orders = []

display_menu()
display_order_options()

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


take_order(menu, orders)

subtotal, discount, final_total = calculate_total(orders)

display_receipt(orders, subtotal, discount, final_total)