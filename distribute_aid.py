def distribute_aid(inventory):
    name = input("Item to distribute: ").strip()

    for item in inventory:
        if item["name"].lower() == name.lower():

            try:
                quantity = int(input("Distribution quantity: "))

                if quantity <= 0:
                    print("quantity must be positive.")
                    return

                if quantity > item["quantity"]:
                    print("insufficient stock.")
                    return

                item["quantity"] -= quantity

                if item["quantity"] == 0:
                    inventory.remove(item)

                print("distribution successful.")
                return

            except ValueError:
                print("Invalid quantity.")
                return

    print("Item not found.")