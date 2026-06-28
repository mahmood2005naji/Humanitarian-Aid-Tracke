def save_inventory(self):    
        with open(self.filename, 'w') as file:
            for item in self.inventory:
                file.write(f"{item['name']},{item['quantity']},{item['donor']}\n")
