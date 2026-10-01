def calculate_total(orders):
    subtotal = 0

    for order in orders:
        subtotal = subtotal + order[3]

    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    final_total = subtotal - discount

    return subtotal, discount, final_total


def display_receipt(orders, subtotal, discount, final_total):
    print()
    print("====================================")
    print("             JOLLIBEE")
    print("          OFFICIAL RECEIPT")
    print("====================================")
    print("Item\t\tQty\tPrice\tTotal")
    print("------------------------------------")

    for order in orders:
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