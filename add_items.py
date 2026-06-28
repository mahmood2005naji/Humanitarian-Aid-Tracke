def add_item(self):
        name = input("Item Name: ").strip()
        donor = input("Donor Organization: ").strip()
        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                return # stop
        except ValueError:
            print("Invalid quantity.")
            return
        for item in self.inventory:
            if item["name"].lower() == name.lower():
                item["quantity"] += quantity
                print("Existing item updated.")
                return
        self.inventory.append({ "name": name, "quantity": quantity, "donor": donor })
        print("New item added.")
        