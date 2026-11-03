(https://github.com/user-attachments/files/34317242/README.md)
# Humanitarian Aid Tracker

A simple command-line program for tracking humanitarian aid inventory: record incoming shipments, distribute aid, search for items, and print an inventory report. Data is saved to a plain text file between runs.

## Features

- **Add shipment:** add a new item, or increase the quantity of an existing one (matching is case-insensitive).
- **Distribute aid:** reduce an item's stock. Items that reach zero are removed from the inventory.
- **Inventory report:** print the full inventory as a table.
- **Search item:** look up an item by name and see its quantity and donor.
- **Save & exit:** write the inventory to `aid_inventory.txt`.

## Requirements

- Python 3.8 or newer
- [pandas](https://pandas.pydata.org/) (used for the report)

```bash
pip install pandas
```

## Usage

```bash
python main.py
```

Menu:

```
===== Humanitarian Aid Tracker =====
1. Add Shipment
2. Distribute Aid
3. Inventory Report
4. Search Item
5. Save & Exit
```

Choose option **5** to save. Changes made in a session are lost if you close the program without saving.

### Example report

```
Inventory Report
--------------------------------------------------
Item Name  Quantity  Donor
    Rice       200   WFP
Blankets        80   Red Cross
--------------------------------------------------
```

## Project structure

| File | Purpose |
|---|---|
| `main.py` | Menu loop and program entry point |
| `load_inventory.py` | Reads the inventory from the data file |
| `save_inventory.py` | Writes the inventory to the data file |
| `add_items.py` | Adds a shipment or updates an existing item |
| `distribute_aid.py` | Distributes stock and removes empty items |
| `search_item.py` | Searches for an item by name |
| `generate_report.py` | Prints the inventory report with pandas |
| `aid_inventory.txt` | Data file, created on first save |

## Data file format

`aid_inventory.txt` stores one item per line as `name,quantity,donor`:

```
Rice,200,WFP
Blankets,80,Red Cross
```

Item and donor names should not contain commas, because the comma is the separator.

## Input rules

- Quantities must be whole numbers greater than zero.
- You cannot distribute more than the available stock.
- Item names are matched ignoring upper and lower case.

## Possible improvements

- Support commas in names by using the `csv` module or JSON.
- Add a low-stock warning.
- Add automated tests.
