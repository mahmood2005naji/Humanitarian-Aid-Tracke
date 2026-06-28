def search_item(inventory):
    name = input("Search item: ").strip()

    for item in inventory:
        if item["name"].lower() == name.lower():

            print("\nItem Found")
            print(f"Name     : {item['name']}")
            print(f"Quantity : {item['quantity']}")
            print(f"Donor    : {item['donor']}")
            return

    print("Item not found.")