def load_inventory(filename):
    inventory = []

    try:
        with open(filename, "r") as file:
            for line in file:
                name, quantity, donor = line.strip().split(",")

                inventory.append({
                    "name": name,
                    "quantity": int(quantity),
                    "donor": donor
                })

    except FileNotFoundError:
        pass

    return inventory