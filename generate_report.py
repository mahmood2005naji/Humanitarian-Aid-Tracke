import pandas as pd

def generate_report(inventory):
    
    if not inventory:
        print("Inventory is empty.")  
        return  

    df = pd.DataFrame(inventory)

    df.columns = ["Item Name", "Quantity", "Donor"]

    print("\nInventory Report")
    print("-" * 50)

    print(df.to_string(index=False))

    print("-" * 50)